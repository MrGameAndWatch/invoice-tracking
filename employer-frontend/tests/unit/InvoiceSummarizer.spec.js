import moment from 'moment'

import InvoiceSummarizer from '@/components/InvoiceSummarizer.vue'

const invoices = [
  {
    userId: 'user1',
    amount: 1.0,
    timestamp: '03/08/2019 12:38:02'
  },
  {
    userId: 'user1',
    amount: 2.5,
    timestamp: '03/08/2020 11:30:00'
  },
  {
    userId: 'user1',
    amount: 5.25,
    timestamp: '30/07/2020 17:33:31'
  },
  {
    userId: 'user2',
    amount: 100.0,
    timestamp: '25/07/2020 14:33:22'
  }
]

const summaryStartDate = moment('01/07/2020', 'DD/MM/YYYY').toDate()
const summaryEndDate = moment('04/08/2020 13:00:00', 'DD/MM/YYYY HH:mm:ss').toDate()

describe('InvoiceSummarizer.vue', () => {
  it('aggregates by date filtered invoices amounts per user correctly', () => {
    const localThis = { invoices: invoices, summaryStartDate: summaryStartDate, summaryEndDate: summaryEndDate }
    const summary = InvoiceSummarizer.computed.invoiceSummary.call(localThis)
    expect(summary).toStrictEqual([{userId: 'user1', refundSum: 7.75}, {userId: 'user2', refundSum: 100.0}])
  })
})
