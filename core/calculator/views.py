from django.shortcuts import render


def home(request):
    expression = ""
    result = ""
    if request.method == "POST":
        expression = request.POST.get("expression", "")
        value = request.POST.get("value")
        operation = request.POST.get("operation")
        if value:
            expression += value
        else:
            match operation:
                case "delete":
                    expression = expression[:-1]
                case "clear":
                    expression = ""
                case "calculate":
                    try:
                        result = eval(expression)
                        expression = str(result)
                    except:
                        result = "Error"
                        expression = ""
                case _:
                    pass
    return render(
        request, "calculator/home.html", {"expression": expression, "result": result}
    )
