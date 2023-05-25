#def create_purchase_receipt(purchase_order,payment_ratio):
#    purchase_receipt = frappe.new_doc("Purchase Receipt")
#    purchase_receipt.update({
#        "supplier": purchase_order.supplier,
#        "company": purchase_order.company,
#        "purchase_order": purchase_order.name,
#        "cost_center": purchase_order.cost_center,
#        "set_posting_time": 0,
#        "set_warehouse": purchase_order.set_warehouse,
#        "taxes_and_charges": purchase_order.taxes_and_charges,
#        "items": [],
#        "taxes": []
#    })
# 
#    # Add Purchase Order items to the Purchase Receipt
#    for po_item in purchase_order.items:
#        purchase_receipt.append("items", {
#            "item_code": po_item.item_code,
#            "purchase_order": po_item.parent,
#            "cost_center": purchase_order.cost_center,
#            "qty": payment_ratio * po_item.qty,
#            "amount": payment_ratio * po_item.amount,
#            "rate": po_item.rate,
#            "uom": po_item.uom,
#            "warehouse": po_item.warehouse,
#            "schedule_date": po_item.schedule_date,
#            "purchase_order_item": po_item.name
#        })
# 
#    for tax in purchase_order.taxes:
#        purchase_receipt.append("taxes", {
#            "category": tax.category,
#            "add_deduct_tax": tax.add_deduct_tax,
#            "charge_type": tax.charge_type,
#            "account_head": tax.account_head,
#            "description": tax.description,
#            "tax_amount": tax.tax_amount * payment_ratio,
#            "rate": tax.rate,
#        })
# 
#    purchase_receipt.save()
#    purchase_receipt.submit()
# 
#    frappe.msgprint("Purchase Receipt created")
