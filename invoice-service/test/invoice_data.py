from src.model.invoice import Invoice, InvoiceBuilder

invoices = [
    InvoiceBuilder()
        .user_id("abc-def-gh-1")
        .description("Hotel im Park")
        .amount(85.50)
        .build(),
    InvoiceBuilder()
        .user_id("abc-gfkdl-dfsa-2")
        .description("Geschäftsessen mit Partner X")
        .amount(200.57)
        .build()
]
