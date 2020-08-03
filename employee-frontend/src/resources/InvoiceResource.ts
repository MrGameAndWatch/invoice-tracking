import axios from 'axios';

export default class InvoiceResource {

    async getInvoices() {
        const response = await axios.get(`http://localhost:5000/invoices`)
        return response.data;
    }

    postInvoice() {
    }
}