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

invoices_for_one_user = [
    InvoiceBuilder()
        .user_id("User1")
        .description("ICE Fahrt nach München")
        .amount(150.76)
        .build(),
    InvoiceBuilder()
        .user_id("User1")
        .description("Hotel in München für zwei Nächte")
        .amount(162.74)
        .build(),
    InvoiceBuilder()
        .user_id("User1")
        .description("Fahrtkosten in München")
        .amount(25.68)
        .build()
]
