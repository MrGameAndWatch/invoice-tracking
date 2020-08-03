import { extend } from 'vee-validate'
import { required } from 'vee-validate/dist/rules'

extend('required', {
  ...required,
  message: 'This field is required.'
})

extend('is_money_decimal', {
    validate: (value) => {
        const regexp = /^\d+(\.\d{1,2})?$/
        return regexp.test(value)
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
        const regexp = /^[A-Za-z]*$/
        return regexp.test(value)
    },
    message: 'The input must be a valid user id (any number of capital and lower case letters without spaces)'
})
