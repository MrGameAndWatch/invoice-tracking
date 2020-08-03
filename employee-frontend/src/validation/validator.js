import { extend } from 'vee-validate'
import { required } from 'vee-validate/dist/rules'
import { isValidMoneyDecimal, isValidUserId } from './validationFunctions.js'

extend('required', {
  ...required,
  message: 'This field is required.'
})

extend('is_money_decimal', {
    validate: (value) => {
        return isValidMoneyDecimal(value)
    },
    message: 'The input must be a monetary amount.'
})

extend('is_positive_monetary_amount', {
    validate: (value) => {
        return Number(value) > 0.0
    },
    message: 'The amount must be greater than 0.'
})

extend('valid_user_id', {
    validate: (value) => {
        return isValidUserId(value)
    },
    message: 'The input must be a valid user id (any number of capital and lower case letters without spaces)'
})
