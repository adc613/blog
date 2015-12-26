(function(){
  var app = angular.module('blogApp', ['ngRoute', 'ngSanitize']);
    
  app.config(function($interpolateProvider, $routeProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $routeProvider
      .when('/entries/:entryID', {
        templateUrl: '/static/angular/detail.html',
        controller: 'DetailController'
      })
      .otherwise({
        redirectTo: '/',
        templateUrl: '/static/angular/list.html',
        controller: 'BlogController'
      });
  });
  
  app.filter('articleFormatter', function(){
    return function(text){
      if(typeof(text) != typeof('string')) text = '';
      splitText = text.split('\n');
      formatedText = '';
      for(i = 0; i < splitText.length; i++){
        formatedText += '<p>' + splitText[i] + '</p>';
      }
      return formatedText;
    }
  })
    
  app.factory('Data', ['$http', function($http) {
    var data = [];
    var promise;

    var req =  {
      method: 'GET',
      url: '/entries/api/entries/?format=json',
    };

    return {
      getData: function(){
        if(!promise){
          
          promise = $http(req).then(
            function(resp){
              data = resp.data;
              return data;
            }, 
            function(resp){
              return resp;
            });
        };
        
        return promise;
        },
      getDetail: function(id) {
        return data[id];
      }
    };
  }]);
    
  app.controller('BlogController', ['$http','$scope', 'Data', function($http, $scope, Data){
    $scope.pageClass = 'page-home';
    Data.getData().then(
      function(data){
        $scope.articles = data;
      },
      function(resp){
        console.log('error....');
        console.log(resp);
      });
  }]);


  app.directive('blogEntry', function() {
    return {
      restrict: 'E',
      templateUrl: '/static/angular/entry.html',
      controller: 'BlogController',
      controllerAs: 'BlogCtrl'
    };
  });
    
  app.directive('blogList', function(){
    return {
      restrict: 'E',
      templateUrl: '/static/angular/blog_list.html',
      controller: 'BlogController',
      controllerAs: 'blogCtrl'
    }
  })
  app.controller('DetailController', ['$scope', '$routeParams', 'Data', function($scope, $routeParams, Data) {
    $scope.pageClass = 'page-about';
    Data.getData().then(
      function(data){
        $scope.entry = data[$routeParams.entryID - 1];
      },
      function(error) {
        console.log('error....');
        console.log(error);
      }
    );
  }]);

})();
