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

\\+ CreateIssue
    * `assetType`: For a list of possible values, see [Asset Types](https://community.perfectomobile.com/Developers/Developer-Library/Concepts/Asset_Type)
    * `projectId`: The oid of the project you want to create the issue for, f.e. Scope:1535
    * `attributes`: Map of key / value pairs
    * `token`: output property - Output token which is the oid reference


## Testing / Building ##


`./gradlew clean assemble`

And copy the `jar` from `build/libs` into your plugins folder.

