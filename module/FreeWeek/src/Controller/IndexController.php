<?php

namespace GamerPowered\FreeWeek\Controller;

use JMS\Serializer\SerializerBuilder;
use Steam\Adapter\Guzzle;
use Steam\Api\PlayerService;
use Steam\Api\User;
use Steam\Configuration;
use Zend\Mvc\Controller\AbstractActionController;
use Zend\View\Model\ViewModel;

/**
 * IndexController
 *
 * @package   GamerPowered\FreeWeek\Controller
 * @author    Martin Meredith <mez@gamerpowered.co.uk>
 * @copyright 2014 Martin Meredith
 */
class IndexController extends AbstractActionController
{
    public function indexAction()
    {
    }
}
