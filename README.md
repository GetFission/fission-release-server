[![Build Status](https://travis-ci.org/GetFission/fission-release-server.svg?branch=master)](https://travis-ci.org/GetFission/fission-release-server)

# [WIP] Fission Electron Release Server

## Motivation

The Fission Release Server makes Electron application release simple and risk free. It does so by providing the following solutions,

1. **Advanced release strategies** - Developers should be able to easily Electron applications via staged rollouts, alpha/beta channels, as well as select specific customer audiences through segmentation. (Eg. Release an application to internal office users only, or release an application to a specific user(s) while triaging critical features/bugfixes).
2. **Simple release rollbacks** - Developers/product managers can rollback a potentially buggy release without customers having to manually downgrade via a pleasant UI.
3. **Powerful release analytics** - As developers we don't want to just 'slowly' rollout our application, we want to know if a new version of a product causes any known regression bugs. Thus application release should be tied to crash reporting / analytics.


## To our community

This project will open source and free to self-host or you can opt-in our managed solution at a monthly subscription at [GetFission](http://getfission.com/)

We will be working towards achieving the aforementioned goals. If you are interested in projects updates / feedback follow me on Twitter [@SimplyAhmazing](https://twitter.com/SimplyAhmaz1ng)


# Wishlist

* Companion auto-updater npm package
* Advanced audience selection
* Manage releases for multiple applications

# Tooling & Getting started

To setup the project locally, check out the [getting started docs](docs/getting-started.md)

To learn about the project tooling checkout the [tooling documentation](docs/tooling.md)


## Contributing

We welcome contributions from the community, given that they respect these basic guidelines:

* All Tests & Static Analysis passing;

If you want to tackle any open issue, well..... Just go for it! :)
