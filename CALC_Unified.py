import tkinter as tk
from tkinter import ttk, messagebox

# ==================================
#   🎨 CONSTANTS AND STYLES
# ==================================

# 🎨 COLOR PALETTE
COLOR_PRIMARY = "#2c71c3"
COLOR_BACKGROUND = "#f5f5f5"
COLOR_ACCENT_BG = "#e8f4f8"
COLOR_SUCCESS = "#28a745"
COLOR_DANGER = "#dc3545"
COLOR_TEXT_NORMAL = "#000000"
COLOR_TEXT_SECONDARY = "#666"

# 🖋 FONT STYLES
FONT_FAMILY = "Arial"
FONT_TITLE = (FONT_FAMILY, 11, "bold")
FONT_ENTRY = (FONT_FAMILY, 13)
FONT_RESULT = (FONT_FAMILY, 13, "bold")
FONT_TAX_RESULT_LARGE = (FONT_FAMILY, 14, "bold")
FONT_BUTTON = (FONT_FAMILY, 10, "bold")

# Global Button Style Dictionary
BUTTON_STYLE = {
    "bg": COLOR_PRIMARY, 
    "fg": "white", 
    "font": FONT_BUTTON, 
    "padx": 15, 
    "pady": 5, 
    "cursor": "hand2"
}

CLEAR_BUTTON_STYLE = {
    "bg": "#6c757d",
    "fg": "white",
    "font": FONT_BUTTON,
    "padx": 15,
    "pady": 5,
    "cursor": "hand2"
}

CLEAR_ALL_BUTTON_STYLE = {
    "bg": COLOR_DANGER,
    "fg": "white",
    "font": FONT_BUTTON,
    "padx": 20,
    "pady": 6,
    "cursor": "hand2"
}

# ==================================
#     ROOT WINDOW SETUP
# ==================================

root = tk.Tk()
root.title("Percentage & Tax Calculator - Unified Edition")
root.geometry("1000x600")
root.configure(bg=COLOR_BACKGROUND)

# ttk Style for Notebook (Modernization)
style = ttk.Style()
style.theme_use('clam')
style.configure('TNotebook.Tab', font=FONT_BUTTON, padding=[10, 5])


# ==================================
#     HELPER WIDGET FUNCTIONS
# ==================================

def create_section_frame(parent, title):
    """Creates a styled section frame with a bold title."""
    frame = tk.Frame(parent, bg="white", padx=15, pady=15, bd=2, relief=tk.GROOVE)
    lbl = tk.Label(frame, text=title, bg="white", font=FONT_TITLE, fg=COLOR_PRIMARY)
    lbl.pack(anchor="w", pady=(0, 10))
    return frame


def create_entry_widget(parent):
    """Creates a standardized entry widget."""
    entry = tk.Entry(parent, width=14, font=FONT_ENTRY, bd=2, relief=tk.GROOVE)
    return entry


def create_clear_button(parent, entry_widgets, result_labels):
    """Creates a clear button to reset entries and results for a specific calculator."""
    
    def clear_fields():
        for entry in entry_widgets:
            entry.delete(0, tk.END)
        for label in result_labels:
            label.config(text="")
            
    btn = tk.Button(parent, text="CLEAR", command=clear_fields, **CLEAR_BUTTON_STYLE)
    return btn


# ==================================
#     GLOBAL CLEAR ALL FUNCTION
# ==================================

def clear_all():
    """Clear all inputs and results across all tabs"""
    # Percentage tab
    entry1_a.delete(0, tk.END)
    entry1_b.delete(0, tk.END)
    result1.config(text="")
    
    entry2_a.delete(0, tk.END)
    entry2_b.delete(0, tk.END)
    result2.config(text="")
    
    entry3_a.delete(0, tk.END)
    entry3_b.delete(0, tk.END)
    result3.config(text="")
    
    entry4_a.delete(0, tk.END)
    entry4_b.delete(0, tk.END)
    result4.config(text="")
    
    # Tax tab
    shared_tax_rate.delete(0, tk.END)
    shared_tax_rate.insert(0, "5.0")  # Reset to default
    
    tax1_price.delete(0, tk.END)
    tax1_result.config(text="")
    tax1_tax_amount.config(text="")
    
    tax2_price.delete(0, tk.END)
    tax2_base_result.config(text="")
    tax2_tax_result.config(text="")


# ==================================
#     HEADER WITH CLEAR ALL BUTTON
# ==================================
header_frame = tk.Frame(root, bg=COLOR_BACKGROUND)
header_frame.pack(fill="x", padx=10, pady=(10, 5))

tk.Label(header_frame, text="Percentage & Tax Calculator", bg=COLOR_BACKGROUND, 
         font=(FONT_FAMILY, 13, "bold"), fg=COLOR_PRIMARY).pack(side="left", padx=5)
tk.Button(header_frame, text="🔄 CLEAR ALL", command=clear_all, **CLEAR_ALL_BUTTON_STYLE).pack(side="right", padx=5)


# ==================================
#        TAB CONTROL
# ==================================
notebook = ttk.Notebook(root)
tab_percentages = tk.Frame(notebook, bg=COLOR_BACKGROUND)
tab_taxes = tk.Frame(notebook, bg=COLOR_BACKGROUND)

notebook.add(tab_percentages, text="Percentage Calculators")
notebook.add(tab_taxes, text="Tax Calculators")
notebook.pack(expand=True, fill="both", padx=10, pady=10)


# =====================================================
#                  TAB 1: PERCENTAGE TOOLS
# =====================================================

# --- 1. What is X% of Y? ---
def calc_1():
    try:
        x = float(entry1_a.get())
        y = float(entry1_b.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in both fields.")
    else:
        result1.config(text=f"{(x/100)*y:.2f}")


frame1 = create_section_frame(tab_percentages, "1. What is X% of Y?")
frame1.pack(fill="x", padx=10, pady=8)

row1 = tk.Frame(frame1, bg="white")
row1.pack()

entry1_a = create_entry_widget(row1)
entry1_a.pack(side="left", padx=5)
tk.Label(row1, text="% of", bg="white", font=FONT_ENTRY).pack(side="left")
entry1_b = create_entry_widget(row1)
entry1_b.pack(side="left", padx=5)
tk.Label(row1, text="=", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tk.Button(row1, text="CALCULATE", command=calc_1, **BUTTON_STYLE).pack(side="left", padx=10)
result1 = tk.Label(row1, text="", bg="white", font=FONT_RESULT, width=12, anchor="w")
result1.pack(side="left", padx=10)
btn_clear1 = create_clear_button(row1, [entry1_a, entry1_b], [result1])
btn_clear1.pack(side="left", padx=5)


# --- 2. X is what percent of Y? ---
def calc_2():
    try:
        x = float(entry2_a.get())
        y = float(entry2_b.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in both fields.")
    else:
        if y == 0:
            return messagebox.showerror("Calculation Error", "Cannot divide by zero (Y cannot be zero).")
        result2.config(text=f"{(x/y)*100:.2f}%")


frame2 = create_section_frame(tab_percentages, "2. X is what percent of Y?")
frame2.pack(fill="x", padx=10, pady=8)

row2 = tk.Frame(frame2, bg="white")
row2.pack()

entry2_a = create_entry_widget(row2)
entry2_a.pack(side="left", padx=5)
tk.Label(row2, text="is what percent of", bg="white", font=FONT_ENTRY).pack(side="left")
entry2_b = create_entry_widget(row2)
entry2_b.pack(side="left", padx=5)
tk.Label(row2, text="=", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tk.Button(row2, text="CALCULATE", command=calc_2, **BUTTON_STYLE).pack(side="left", padx=10)
result2 = tk.Label(row2, text="", bg="white", font=FONT_RESULT, width=12, anchor="w")
result2.pack(side="left", padx=10)
btn_clear2 = create_clear_button(row2, [entry2_a, entry2_b], [result2])
btn_clear2.pack(side="left", padx=5)


# --- 3. Percentage change from X to Y ---
def calc_3():
    try:
        old = float(entry3_a.get())
        new = float(entry3_b.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in both fields.")
    else:
        if old == 0:
            return messagebox.showerror("Calculation Error", "Old value (X) cannot be zero.")
        change = ((new - old) / old) * 100
        result3.config(text=f"{change:+.2f}%")
        result3.config(fg=COLOR_SUCCESS if change >= 0 else COLOR_DANGER)


frame3 = create_section_frame(tab_percentages, "3. Percentage increase/decrease from X to Y")
frame3.pack(fill="x", padx=10, pady=8)

row3 = tk.Frame(frame3, bg="white")
row3.pack()

entry3_a = create_entry_widget(row3)
entry3_a.pack(side="left", padx=5)
tk.Label(row3, text="to", bg="white", font=FONT_ENTRY).pack(side="left")
entry3_b = create_entry_widget(row3)
entry3_b.pack(side="left", padx=5)
tk.Label(row3, text="=", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tk.Button(row3, text="CALCULATE", command=calc_3, **BUTTON_STYLE).pack(side="left", padx=10)
result3 = tk.Label(row3, text="", bg="white", font=FONT_RESULT, width=12, anchor="w")
result3.pack(side="left", padx=10)
btn_clear3 = create_clear_button(row3, [entry3_a, entry3_b], [result3])
btn_clear3.pack(side="left", padx=5)


# --- 4. If X is Y%, what is the whole (100%)? ---
def calc_4():
    try:
        part = float(entry4_a.get())
        percent = float(entry4_b.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in both fields.")
    else:
        if percent == 0:
            return messagebox.showerror("Calculation Error", "Percentage cannot be zero.")
        whole = (part / percent) * 100
        result4.config(text=f"{whole:.2f}")


frame4 = create_section_frame(tab_percentages, "4. If X is Y%, what is the whole (100%)?")
frame4.pack(fill="x", padx=10, pady=8)

row4 = tk.Frame(frame4, bg="white")
row4.pack()

entry4_a = create_entry_widget(row4)
entry4_a.pack(side="left", padx=5)
tk.Label(row4, text="is", bg="white", font=FONT_ENTRY).pack(side="left")
entry4_b = create_entry_widget(row4)
entry4_b.pack(side="left", padx=5)
tk.Label(row4, text="% of", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tk.Label(row4, text="=", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tk.Button(row4, text="CALCULATE", command=calc_4, **BUTTON_STYLE).pack(side="left", padx=10)
result4 = tk.Label(row4, text="", bg="white", font=FONT_RESULT, width=12, anchor="w")
result4.pack(side="left", padx=10)
btn_clear4 = create_clear_button(row4, [entry4_a, entry4_b], [result4])
btn_clear4.pack(side="left", padx=5)


# =====================================================
#                  TAB 2: TAX CALCULATORS
# =====================================================

# Shared tax rate entry
tax_rate_frame = tk.Frame(tab_taxes, bg=COLOR_ACCENT_BG, padx=15, pady=12, bd=2, relief=tk.GROOVE)
tax_rate_frame.pack(fill="x", padx=10, pady=10)

tk.Label(tax_rate_frame, text="Tax Rate:", bg=COLOR_ACCENT_BG, font=FONT_TITLE, fg=COLOR_PRIMARY).pack(side="left", padx=5)
shared_tax_rate = create_entry_widget(tax_rate_frame)
shared_tax_rate.pack(side="left", padx=5)
shared_tax_rate.insert(0, "5.0")
tk.Label(tax_rate_frame, text="%", bg=COLOR_ACCENT_BG, font=FONT_TITLE).pack(side="left")
tk.Label(tax_rate_frame, text="(This rate applies to both calculators below)", 
         bg=COLOR_ACCENT_BG, font=(FONT_FAMILY, 9, "italic"), fg=COLOR_TEXT_SECONDARY).pack(side="left", padx=15)


# -------------------------
#   1. PRICE + TAX
# -------------------------
def calc_price_with_tax():
    try:
        price = float(tax1_price.get())
        tax = float(shared_tax_rate.get())
    except ValueError:
        return messagebox.showerror("Input Error", "Enter valid numbers for price and tax rate.")
    else:
        total = price * (1 + tax / 100)
        tax_amount = price * (tax / 100)
        tax1_result.config(text=f"AED {total:.2f}")
        tax1_tax_amount.config(text=f"(Tax: AED {tax_amount:.2f})")


frame_t1 = create_section_frame(tab_taxes, "1. Add Tax to Base Price")
frame_t1.pack(fill="x", padx=10, pady=8)

row_t1 = tk.Frame(frame_t1, bg="white")
row_t1.pack(pady=5)

tk.Label(row_t1, text="Base Price: AED", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tax1_price = create_entry_widget(row_t1)
tax1_price.pack(side="left", padx=5)

tk.Label(row_t1, text="→", bg="white", font=("Arial", 14, "bold"), fg=COLOR_PRIMARY).pack(side="left", padx=10)

tk.Button(row_t1, text="CALCULATE", command=calc_price_with_tax, **BUTTON_STYLE).pack(side="left", padx=10)

tk.Label(row_t1, text="Total:", bg="white", font=FONT_TITLE).pack(side="left", padx=(15, 5))
tax1_result = tk.Label(row_t1, text="", bg="white", font=FONT_TAX_RESULT_LARGE, fg=COLOR_SUCCESS, width=10, anchor="w")
tax1_result.pack(side="left")
tax1_tax_amount = tk.Label(row_t1, text="", bg="white", font=(FONT_FAMILY, 9, "italic"), fg=COLOR_TEXT_SECONDARY)
tax1_tax_amount.pack(side="left", padx=5)

btn_clear_t1 = create_clear_button(row_t1, [tax1_price], [tax1_result, tax1_tax_amount])
btn_clear_t1.pack(side="left", padx=5)


# -------------------------
#   2. EXTRACT TAX FROM FINAL PRICE
# -------------------------
def calc_extract_tax():
    try:
        final = float(tax2_price.get())
        tax = float(shared_tax_rate.get())
    except ValueError:
        return messagebox.showerror("Input Error", "Enter valid numbers for final price and tax rate.")
    else:
        base = final / (1 + tax / 100)
        tax_amount = final - base
        tax2_base_result.config(text=f"AED {base:.2f}")
        tax2_tax_result.config(text=f"AED {tax_amount:.2f}")


frame_t2 = create_section_frame(tab_taxes, "2. Extract Tax from Final Price")
frame_t2.pack(fill="x", padx=10, pady=8)

row_t2 = tk.Frame(frame_t2, bg="white")
row_t2.pack(pady=5)

tk.Label(row_t2, text="Final Price: AED", bg="white", font=FONT_ENTRY).pack(side="left", padx=5)
tax2_price = create_entry_widget(row_t2)
tax2_price.pack(side="left", padx=5)

tk.Label(row_t2, text="→", bg="white", font=("Arial", 14, "bold"), fg=COLOR_PRIMARY).pack(side="left", padx=10)

tk.Button(row_t2, text="CALCULATE", command=calc_extract_tax, **BUTTON_STYLE).pack(side="left", padx=10)

result_container = tk.Frame(row_t2, bg="white")
result_container.pack(side="left", padx=15)

tk.Label(result_container, text="Base:", bg="white", font=FONT_TITLE).pack(side="left", padx=(0, 5))
tax2_base_result = tk.Label(result_container, text="", bg="white", font=FONT_TAX_RESULT_LARGE, fg=COLOR_SUCCESS, width=9, anchor="w")
tax2_base_result.pack(side="left", padx=5)

tk.Label(result_container, text="Tax:", bg="white", font=FONT_TITLE).pack(side="left", padx=(20, 5))
tax2_tax_result = tk.Label(result_container, text="", bg="white", font=FONT_TAX_RESULT_LARGE, fg=COLOR_DANGER, width=9, anchor="w")
tax2_tax_result.pack(side="left", padx=5)

btn_clear_t2 = create_clear_button(row_t2, [tax2_price], [tax2_base_result, tax2_tax_result])
btn_clear_t2.pack(side="left", padx=5)


root.mainloop()
