'use strict'
module.exports = {
  AUTH0_DOMAIN: JSON.stringify(process.env.AUTH0_DOMAIN),
  AUTH0_REDIRECT_URI: JSON.stringify(process.env.AUTH0_REDIRECT_URI),
  JWT_AUDIENCE: JSON.stringify(process.env.JWT_AUDIENCE),
  NODE_ENV: '"production"'
}
