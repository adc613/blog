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
      splitText = text.split('\n');
      formatedText = '<p>';
      for(i = 0; i < splitText.length; i++){
        formatedText += splitText[i] + '</p><p>';
      }
      formatedText += '</p>';
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
              /*
              console.log(data.length);
              console.log(data);
              for(i = 0; i < data.length; i++){
                console.log(i);
                
               // console.log(formatText(data[i].article));
                //formatText(data[i].article);
                //article = data[i].article;
                //article = formatText(article);
                //data[i].article = article;
              }
             */
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
    
    function formatText(data) {
    //console.log(text);
      for(i = 0; i < data.length; i++){
        console.log(i);
        //console.log(data);
        //text = data[i].article;
        //console.log(text);
        /*
        splitText = text.split('\n');
       
        */
        //data[i].article = formatedText;
      }
      
      return data;
    }
    
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
    
  app.controller('DetailController', ['$scope', '$routeParams', 'Data', function($scope, $routeParams, Data) {
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
