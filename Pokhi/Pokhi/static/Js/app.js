﻿
var app = angular.module('Pokhi', ['ui.router']);

    app.config(function ($stateProvider) {
        $stateProvider
        .state('home', {
            url : '/',
            templateUrl: '/Views/Home.html',
            controller: 'HomeController'
        })
        .state('base', {
            url: '/base',
            templateUrl: '/Views/Base.html',
            controller: 'BaseController'
        })
        .state('PongApp', {
            url: '/app/pong',
            templateUrl: '/Apps/Pong/index.html',
        })
        .state("otherwise", {
            url: '/',
            templateUrl: '/Views/Home.html',
            controller: 'HomeController'
        })
    });

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });

