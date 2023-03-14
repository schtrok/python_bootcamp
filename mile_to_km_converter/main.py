import tkinter


def miles_to_km(miles: float) -> float:
    return miles * 1.60934


def calculate(output, input):
    output["text"] = str(miles_to_km(float(input.get())))


window = tkinter.Tk()
window.geometry("600x400")


# input
input = tkinter.Entry()

# labels
mile_label = tkinter.Label(text="Miles")
km_label = tkinter.Label(text="Km")
is_equal_to = tkinter.Label(text="is equal to")
result = tkinter.Label(text="0")

# button
btn = tkinter.Button(text="Calculate", command=lambda: calculate(result, input))


positions = [
    (input, 1, 0),
    (mile_label, 2, 0),
    (km_label, 2, 1),
    (is_equal_to, 0, 1),
    (result, 1, 1),
    (btn, 2, 1),
]

for element, column, row in positions:
    element.grid(column=column, row=row)

window.mainloop()
