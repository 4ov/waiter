

chunks = {
    "1": "١",
    "2": "٢",
    "3": "٣",
    "4": "٤",
    "5": "٥",
    "6": "٦",
    "7": "٧",
    "8": "٨",
    "9": "٩",

    "10": "١٠",
    "11": "١١",
    "12": "١٢",
    "13": "١٣",
    "14": "١٤",
    "15": "١٥",
    "16": "١٦",
    "17": "١٧",
    "18": "١٨",
    "19": "١٩",

    "20": "٢٠",
    "30": "٣٠",
    "40": "٤٠",
    "50": "٥٠",
    "60": "٦٠",
    "70": "٧٠",
    "80": "٨٠",
    "90": "٩٠",

    "100": "١٠٠",
    "200": "٢٠٠",
    "300": "٣٠٠",
    "400": "٤٠٠",
    "500": "٥٠٠",
    "600": "٦٠٠",
    "700": "٧٠٠",
    "800": "٨٠٠",
    "900": "٩٠٠",

    "1000": "١٠٠٠",
    "2000": "٢٠٠٠",
    "3000": "٣٠٠٠",
    "4000": "٤٠٠٠",
    "5000": "٥٠٠٠",
    "6000": "٦٠٠٠",
    "7000": "٧٠٠٠",
    "8000": "٨٠٠٠",
    "9000": "٩٠٠٠",


    "w": "شِبّاكْ رَقمْ",
    "c": "عَميلْ رَقمْ",
    "a": "و"
}

say_map = dict(map(lambda v: (v, f"./chunks/{v}.mp3"), chunks.keys()))
