(function(){
    var app = angular.module('blogApp', []);
    app.config(function($interpolateProvider, $sceProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
        $sceProvider.enabled(false);
    });

    /*
    app.config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/entries/:entry', {
                templateUrl: 'detail.html',
                controller: 'blogController'
            }).
            otherwise({
                redirectTo: '/'
            });
        }]);
        */

    app.controller('blogController', ['$http','$scope', function($http, $scope){
        $scope.articles = []

        var req =  {
            method: 'GET',
            url: 'http://localhost:8080/entries/api/entries/?format=json',
        };

        $http(req).then(function(resp){
            $scope.articles = resp.data;
        }, 
        function(resp){
            console.log('Error...');
            console.log(resp);
        });
    }]);

    app.directive('blogEntry', function() {
        return {
            restrict: 'E',
            templateUrl: '/static/js/entry.html',
            controller: 'blogController',
            controllerAs: 'blogCtrl'
        };
    });

})();
