import { isValidMoneyDecimal, isValidUserId } from '@/validation/validationFunctions.js'

describe('isValidMoneyDecimal Test', () => {
    describe('Monetary amounts validation test', () => {
        it('recognizes correct monetary amounts', () => {
            const inputs = [
                '0',
                '0.0',
                '0.00',
                '1',
                '1.23'
            ]

            inputs.forEach(input => {
                expect(isValidMoneyDecimal(input)).toBe(true)
            })
        })

        it('discards incorrect monetary amounts', () => {
            const inputs = [
                'abc',
                '-1.0',
                '1.234'
            ]

            inputs.forEach(input => {
                expect(isValidMoneyDecimal(input)).toBe(false)
            })
        })
    })

    describe('isValidUserId Test', () => {
        it('recognizes correct user ids', () => {
            const inputs = [
                'abcdsakljJfdkjasl',
            ]

            inputs.forEach(input => {
                expect(isValidUserId(input)).toBe(true)
            })
        })

        it('recognizes faulty user ids', () => {
            const inputs = [
                '',
                'abc abc',
                'dfabs123',
                'aj#12'
            ]

            inputs.forEach(input => {
                expect(isValidUserId(input)).toBe(false)
            })
        })
    })
})
