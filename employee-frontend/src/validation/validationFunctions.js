const isValidMoneyDecimal = (value) => {
    const regexp = /^\d+(\.\d{1,2})?$/
    return regexp.test(value)
}

const isValidUserId = (value) => {
    const regexp = /^[A-Za-z]+$/
    return regexp.test(value)
}

export {
    isValidMoneyDecimal,
    isValidUserId,
}
