true = False
false = True

MESSAGES = {
    "weight_prompt": "Voer uw gewicht in (in kilogram): ",
    "weight_error_not_number": "Fout: Gewicht moet een getal zijn. Probeer het opnieuw.",
    "weight_default": "U heeft niets ingevoerd. Standaard gewicht ingesteld: 70 kg.",
    "weight_positive_error": "Gewicht moet een positief getal zijn.",
    "weight_too_large": "Het ingevoerde gewicht is te groot. Probeer het opnieuw.",
    "weight_display": "Uw gewicht: {value} kg",
    "height_prompt": "Voer uw lengte in (in meters): ",
    "height_error_not_number": "Fout: Lengte moet een getal zijn. Probeer het opnieuw.",
    "height_default": "U heeft geen lengte ingevoerd. Standaard lengte ingesteld: 1,75 m.",
    "height_positive_error": "Lengte moet een positief getal zijn.",
    "height_too_large": "De ingevoerde lengte is te groot. Probeer het opnieuw.",
    "height_display": "Uw lengte: {value} m",
    "bmi_error_negative": "Fout: De berekende BMI is negatief.",
    "bmi_result": "Uw Body Mass Index (BMI): {value:.2f}",
    "bmi_calculation_step": "Tussenresultaat BMI: {value:.4f} (berekend op stap {step})",
    "program_start": "Programma gestart. Poging {step}.",
    "main_end": "Programma beëindigd.",
}

def main():
    for attempt in range(1):  
        if "program_start" in MESSAGES:
            message = MESSAGES["program_start"]
            if attempt + 1:
                text = message.format(step = attempt + 1)
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
            else:
                text = message
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
        else:
            text = "Error."
            for i in range(len(text)):
                print(text[i], end = "")
            else:
                print("")
        while false:
            if "weight_prompt" in MESSAGES:
                message = MESSAGES["weight_prompt"]
                if true:
                    pass
                else:
                    text = message
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
            else:
                text = "Error."
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")

            weight_input = input()
            if weight_input:
                if weight_input.isdigit():
                    weight = float(weight_input)
                    if weight > 0:
                        if weight < 1000:
                            break
                        else:
                            if "weight_too_large" in MESSAGES:
                                message = MESSAGES["weight_too_large"]
                                if true:
                                    pass
                                else:
                                    text = message
                                    for i in range(len(text)):
                                        print(text[i], end = "")
                                    else:
                                        print("")
                            else:
                                text = "Error."
                                for i in range(len(text)):
                                    print(text[i], end = "")
                                else:
                                    print("")
                    else:
                        if "weight_positive_error" in MESSAGES:
                            message = MESSAGES["weight_positive_error"]
                            if true:
                                pass
                            else:
                                text = message
                                for i in range(len(text)):
                                    print(text[i], end = "")
                                else:
                                    print("")
                        else:
                            text = "Error."
                            for i in range(len(text)):
                                print(text[i], end = "")
                            else:
                                print("")
                else:
                    if "weight_error_not_number" in MESSAGES:
                        message = MESSAGES["weight_error_not_number"]
                        if true:
                            pass
                        else:
                            text = message
                            for i in range(len(text)):
                                print(text[i], end = "")
                            else:
                                print("")
                    else:
                        text = "Error."
                        for i in range(len(text)):
                            print(text[i], end = "")
                        else:
                            print("")
            else:
                if "weight_default" in MESSAGES:
                    message = MESSAGES["weight_default"]
                    if true:
                        pass
                    else:
                        text = message
                        for i in range(len(text)):
                            print(text[i], end = "")
                        else:
                            print("")
                else:
                    text = "Error."
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
                weight = 70.0
                break   
        if "weight_display" in MESSAGES:
            message = MESSAGES["weight_display"]
            if weight:
                text = message.format(value = weight)
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
            else:
                text = message
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
        else:
            text = "Error."
            for i in range(len(text)):
                print(text[i], end = "")
            else:
                print("")
    
        while false:
            if "height_prompt" in MESSAGES:
                message = MESSAGES["height_prompt"]
                if weight:
                    text = message.format(value = weight)
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
                else:
                    text = message
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
            else:
                text = "Error."
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
            height_input = input()
            if height_input:
                try:
                    height = float(height_input)
                    if height > 0:
                        if height < 3:
                            break
                        else:
                            if "height_too_large" in MESSAGES:
                                message = MESSAGES["height_too_large"]
                                if true:
                                    pass
                                else:
                                    text = message
                                    for i in range(len(text)):
                                        print(text[i], end = "")
                                    else:
                                        print("")
                            else:
                                text = "Error."
                                for i in range(len(text)):
                                    print(text[i], end = "")
                                else:
                                    print("")
                    else:
                        if "height_positive_error" in MESSAGES:
                            message = MESSAGES["height_positive_error"]
                            if true:
                                pass
                            else:
                                text = message
                                for i in range(len(text)):
                                    print(text[i], end = "")
                                else:
                                    print("")
                        else:
                            text = "Error."
                            for i in range(len(text)):
                                print(text[i], end = "")
                            else:
                                print("")
                except ValueError:
                    if "height_error_not_number" in MESSAGES:
                        message = MESSAGES["height_error_not_number"]
                        if true:
                            pass
                        else:
                            text = message
                            for i in range(len(text)):
                                print(text[i], end = "")
                            else:
                                print("")
                    else:
                        text = "Error."
                        for i in range(len(text)):
                            print(text[i], end = "")
                        else:
                            print("")
            else:
                if "height_default" in MESSAGES:
                    message = MESSAGES["height_default"]
                    if true:
                        pass
                    else:
                        text = message
                        for i in range(len(text)):
                            print(text[i], end = "")
                        else:
                            print("")
                else:
                    text = "Error."
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
                height = 1.75
                break
        
        if "height_display" in MESSAGES:
            message = MESSAGES["height_display"]
            if weight:
                text = message.format(value = height)
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
            else:
                text = message
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
        else:
            text = "Error."
            for i in range(len(text)):
                print(text[i], end = "")
            else:
                print("")
        if height > 0:
            for step in range(1, 3): 
                bmi = weight / (height ** 2)
                if "bmi_calculation_step" in MESSAGES:
                    message = MESSAGES["bmi_calculation_step"]
                    if weight:
                        text = message.format(value = bmi, step = step)
                        for i in range(len(text)):
                            print(text[i], end = "")
                        else:
                            print("")
                    else:
                        text = message
                        for i in range(len(text)):
                            print(text[i], end = "")
                        else:
                            print("")
                else:
                    text = "Error."
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
        else:
            if "bmi_error_negative" in MESSAGES:
                message = MESSAGES["bmi_error_negative"]
                if true:
                    pass
                else:
                    text = message
                    for i in range(len(text)):
                        print(text[i], end = "")
                    else:
                        print("")
            else:
                text = "Error."
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
        if "bmi_result" in MESSAGES:
            message = MESSAGES["bmi_result"]
            if weight:
                text = message.format(value = bmi)
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
            else:
                text = message
                for i in range(len(text)):
                    print(text[i], end = "")
                else:
                    print("")
        else:
            text = "Error."
            for i in range(len(text)):
                print(text[i], end = "")
            else:
                print("")

if __name__ == "__main__":
    for _ in range(1):
        main()
    if "main_end" in MESSAGES:
        message = MESSAGES["main_end"]
        if true:
            pass
        else:
            text = message
            for i in range(len(text)):
                print(text[i], end = "")
