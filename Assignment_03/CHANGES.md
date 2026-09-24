# Assignment 03 — CHANGES

**Name:** _______SAI WANNA HTOO_______________  **Student ID:** ____________6705140028__________

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | *e.g. product stored as a bare tuple `("Laptop", 1200.0, "electronics")`* | *`Product` class with `name`, `price`, `category`* | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | *e.g. repeated `if tier == ...` for discount and points* | *`Gold`/`Silver`/… subclasses with `discount_rate()` and `points_mult`* | Polymorphism | PASS |
| 3 | Magic numbers such as 0.07, 100, 10, 0.03, and "-" * 40 were written directly in the code. | Replace magic numbers with named constants such as TAX_RATE, DISCOUNT_THRESHOLD, BULK_QTY_THRESHOLD, BULK_DISCOUNT_RATE, POINTS_DIVISOR, and RECEIPT_SEPARATOR. Added TAX_RATES to map product categories to their tax rates. | Clean code / constants | Not needed
| 4 |  Products and order items were stored as tuples in messy codes  | Created a Product class and OrderItem class with constructor validation and calculation methods | Classes / encapsulation 
| 5 |  The original used if/elif chains for each customer tier's discount and points. | Made a Customer base class with Silver, Gold, and Platinum subclasses, each with its own discount and points multiplier. | Polymorphism | Not needed  
| 6 | The original calc() function handled the whole order using tuple data and mixed calculations with printing. | Created an Order class with a Customer and multiple OrderItem objects. Added separate subtotal(), discount(), tax(), total(), points(), and receipt() methods. | Composition / encapsulation / I/O |
## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> The changes that improved the code the most were creating the Customer class family and the Order class. The Customer subclasses made the discount and points rules easier to understand because each customer tier has its own behaviour instead of using long if/elif chains. The Order class also made the program more organized by keeping the customer, items, calculations, and receipt generation together. Keeping the behaviour identical made me especially careful when rewriting the receipt generation and `build_orders()` because they had to produce the same receipt format, values, order of lines, and orders as the original program. I also had to check that the new object-based structure still produced exactly the same final output as the original.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Refactor this tier discount if/elif into subclasses"* | *Base `Customer` + 4 subclasses* | Edited (renamed methods) | Self-test PASS; read every line |
| 2 |  Where to start my edit and and assignment  and where not to touch, tell by line blocks | line 92 - 183 do not touch and start writing at 224 | Okay | i read the 92-183 and after 224
| 3 |  Explain how the golden output comparison works| Explained capture(), GOLDEN_OUTPUT, and your_output == GOLDEN_OUTPUT.| Read the code and verified the comparison flow.
| 4 |  explain how the customer discount rules should be implemented using the discount threshold?|  Explained the subtotal threshold and how each customer tier has different discount rates above and below it.|  Edited (renamed methods)  |
| 5 | explain the legacy code in simple terms | read them 
| 6 | Asked AI to carefully explain how to complete the `receipt()`, `build_orders()`, and `refactored_main()` sections while keeping the original behaviour unchanged. | Explained the purpose and structure of each section and how they connect the refactored classes. | Accepted | Read and checked the explanation against the code and assignment requirements. |
**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.
