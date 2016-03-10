# Preface #

This document describes the functionality provided by the xlr-perfectomobile-plugin.

See the **XL Release Reference Manual** for background information on XL Release and release concepts.

# CI status #

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-perfectomobile-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-perfectomobile\-plugin)

# Overview #

## Requirements ##

* From version 1.0.0+: XLR 4.8.0+

## Installation ##

* Place the `jar` into plugins
* Place the perfectomobile java sdk into plugins (download from [Perfecto Mobile Repository](http://repository-perfectomobile.forge.cloudbees.com/public/com/perfectomobile/http-client/5.6.0.2/)).

## Types ##

+ ListDevices
    * `availableTo`: Define the username to list the devices available to.
    * `devices`: (Output property) List of available devices (deviceId, available).


## Testing / Building ##


`./gradlew clean assemble`

And copy the `jar` from `build/libs` into your plugins folder.

