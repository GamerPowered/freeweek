<?php

return [
    'routes' => [
        'default' => [
            'type' => 'Literal',
            'options' => [
                'route' => '/',
                'defaults' => [
                    'controller' => 'index',
                    'action' => 'index'
                ],
            ],
        ],
        'json' => [
            'type' => 'Segment',
            'options' => [
                'route' => '/json/:action',
                'defaults' => [
                    'controller' => 'json'
                ],
            ],
        ],
    ],
];
