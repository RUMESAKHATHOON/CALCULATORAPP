import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Calculator state
        self.current_operand = "0"
        self.previous_operand = ""
        self.operation = None
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind('<KeyPress>', self.key_press)
        self.root.focus_set()
        
        # Update display initially
        self.update_display()
    
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg='#34495e')
        display_frame.pack(fill='x', padx=10, pady=10)
        
        # Previous operand display
        self.previous_display = tk.Label(
            display_frame,
            text="",
            font=('Arial', 12),
            bg='#34495e',
            fg='#bdc3c7',
            anchor='e',
            height=1,
            padx=10,
            pady=5
        )
        self.previous_display.pack(fill='x')
        
        # Current operand display
        self.current_display = tk.Label(
            display_frame,
            text="0",
            font=('Arial', 24, 'bold'),
            bg='#34495e',
            fg='white',
            anchor='e',
            height=2,
            padx=10,
            pady=5
        )
        self.current_display.pack(fill='x')
    
    def create_buttons(self):
        # Button frame
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Create all buttons individually for better control
        
        # Row 1: AC, ⌫, /, ×
        tk.Button(button_frame, text='AC', font=('Arial', 16, 'bold'), bg='#e74c3c', fg='white',
                 command=self.clear_all).grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='⌫', font=('Arial', 16, 'bold'), bg='#e74c3c', fg='white',
                 command=self.delete_last).grid(row=0, column=1, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='/', font=('Arial', 16, 'bold'), bg='#3498db', fg='white',
                 command=lambda: self.choose_operation('/')).grid(row=0, column=2, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='×', font=('Arial', 16, 'bold'), bg='#3498db', fg='white',
                 command=lambda: self.choose_operation('*')).grid(row=0, column=3, sticky='nsew', padx=2, pady=2)
        
        # Row 2: 7, 8, 9, -
        tk.Button(button_frame, text='7', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('7')).grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='8', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('8')).grid(row=1, column=1, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='9', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('9')).grid(row=1, column=2, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='-', font=('Arial', 16, 'bold'), bg='#3498db', fg='white',
                 command=lambda: self.choose_operation('-')).grid(row=1, column=3, sticky='nsew', padx=2, pady=2)
        
        # Row 3: 4, 5, 6, +
        tk.Button(button_frame, text='4', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('4')).grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='5', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('5')).grid(row=2, column=1, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='6', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('6')).grid(row=2, column=2, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='+', font=('Arial', 16, 'bold'), bg='#3498db', fg='white',
                 command=lambda: self.choose_operation('+')).grid(row=2, column=3, sticky='nsew', padx=2, pady=2)
        
        # Row 4: 1, 2, 3, = (spans 2 rows)
        tk.Button(button_frame, text='1', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('1')).grid(row=3, column=0, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='2', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('2')).grid(row=3, column=1, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='3', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('3')).grid(row=3, column=2, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='=', font=('Arial', 16, 'bold'), bg='#27ae60', fg='white',
                 command=self.compute).grid(row=3, column=3, rowspan=2, sticky='nsew', padx=2, pady=2)
        
        # Row 5: 0 (spans 2 columns), .
        tk.Button(button_frame, text='0', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('0')).grid(row=4, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)
        tk.Button(button_frame, text='.', font=('Arial', 16, 'bold'), bg='#95a5a6', fg='white',
                 command=lambda: self.append_number('.')).grid(row=4, column=2, sticky='nsew', padx=2, pady=2)
        
        # Configure grid weights for responsive design
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def format_number(self, number):
        """Format number for display"""
        try:
            # Convert to float to handle calculations
            num = float(number)
            
            # If it's a whole number, display as integer
            if num == int(num):
                return str(int(num))
            else:
                # Format with up to 10 decimal places, removing trailing zeros
                formatted = f"{num:.10f}".rstrip('0').rstrip('.')
                return formatted
        except:
            return str(number)
    
    def update_display(self):
        """Update the calculator display"""
        # Update current operand display
        display_number = self.format_number(self.current_operand)
        self.current_display.config(text=display_number)
        
        # Update previous operand display
        if self.operation and self.previous_operand:
            operation_symbol = '×' if self.operation == '*' else self.operation
            prev_formatted = self.format_number(self.previous_operand)
            self.previous_display.config(text=f"{prev_formatted} {operation_symbol}")
        else:
            self.previous_display.config(text="")
    
    def append_number(self, number):
        """Add a number or decimal point to current operand"""
        if number == '.' and '.' in self.current_operand:
            return
        
        if self.current_operand == '0' and number != '.':
            self.current_operand = number
        else:
            self.current_operand += number
        
        self.update_display()
    
    def choose_operation(self, next_operation):
        """Set the operation and prepare for next operand"""
        if not self.current_operand:
            return
        
        if self.previous_operand and self.operation:
            self.compute()
        
        self.operation = next_operation
        self.previous_operand = self.current_operand
        self.current_operand = ""
        self.update_display()
    
    def compute(self):
        """Perform the calculation"""
        if not self.previous_operand or not self.current_operand or not self.operation:
            return
        
        try:
            prev = float(self.previous_operand)
            current = float(self.current_operand)
            
            if self.operation == '+':
                result = prev + current
            elif self.operation == '-':
                result = prev - current
            elif self.operation == '*':
                result = prev * current
            elif self.operation == '/':
                if current == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = prev / current
            else:
                return
            
            # Update current operand with result
            self.current_operand = str(result)
            self.operation = None
            self.previous_operand = ""
            self.update_display()
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
            self.clear_all()
    
    def clear_all(self):
        """Clear all calculator state"""
        self.current_operand = "0"
        self.previous_operand = ""
        self.operation = None
        self.update_display()
    
    def delete_last(self):
        """Delete the last entered character"""
        if len(self.current_operand) <= 1:
            self.current_operand = "0"
        else:
            self.current_operand = self.current_operand[:-1]
        self.update_display()
    
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        
        # Numbers and decimal point
        if key.isdigit() or key == '.':
            self.append_number(key)
        # Operations
        elif key in ['+', '-', '*', '/']:
            self.choose_operation(key)
        # Equals or Enter
        elif key in ['='] or event.keysym == 'Return':
            self.compute()
        # Escape for clear
        elif event.keysym == 'Escape':
            self.clear_all()
        # Backspace
        elif event.keysym == 'BackSpace':
            self.delete_last()
    
    def run(self):
        """Start the calculator"""
        self.root.mainloop()

# Create and run the calculator
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()