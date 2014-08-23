<?php

namespace GamerPowered\FreeWeek\Mvc\View\Http;

use Zend\Mvc\View\Http\InjectTemplateListener as ZendInjectTemplateListener;

/**
 * InjectTemplateListener
 *
 * @package   GamerPowered\FreeWeek\Mvc\View\Http
 * @author    Martin Meredith <mez@gamerpowered.co.uk>
 * @copyright 2014 Martin Meredith
 */
class InjectTemplateListener extends ZendInjectTemplateListener
{
    protected function deriveModuleNamespace($controller)
    {
        if (!strstr($controller, '\\')) {
            return '';
        }

        $parts = explode('\\', $controller);

        return $parts[1];
    }
}
