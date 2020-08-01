from src.model.invoice import Invoice, InvoiceBuilder

invoices = [
    InvoiceBuilder()
        .description("Hotel im Park")
        .amount(85.50)
        .build(),
    InvoiceBuilder()
        .description("Geschäftsessen mit Partner X")
        .amount(200.57)
        .build()
]
