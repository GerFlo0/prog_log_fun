def format_and_truncate(value, decimals=2):
    try:
        if isinstance(value, str):
            value = value.replace(",", "")
        num = float(value)
        
        factor = 10 ** decimals
        truncated_num = int(num * factor) / factor
        
        integer_part, _, decimal_part = f"{truncated_num:.{decimals}f}".partition(".")
        formatted_integer = f"{int(integer_part):,}"
        
        if "." in str(value):
            return f"{formatted_integer}.{decimal_part}"
        else:
            return formatted_integer
    except (ValueError, TypeError) as e:
        return f"Error: Entrada inválida ({e})"