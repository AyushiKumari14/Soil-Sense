# =========================================================
# CROP AND PLANT DATABASE
# =========================================================
# These are simplified educational/project ranges.
# Actual suitability depends on soil type, crop variety,
# crop stage, climate and farming method.

CROP_DATA = [

    # =====================================================
    # CEREALS
    # =====================================================

    {
        "name": "Rice",
        "category": "Cereal",
        "min_moisture": 65,
        "max_moisture": 100,
        "min_ph": 5.0,
        "max_ph": 7.0,
        "min_temp": 20,
        "max_temp": 35,
        "water_need": "Very High",
        "description": "Prefers high moisture and warm growing conditions."
    },

    {
        "name": "Wheat",
        "category": "Cereal",
        "min_moisture": 40,
        "max_moisture": 65,
        "min_ph": 6.0,
        "max_ph": 7.5,
        "min_temp": 10,
        "max_temp": 25,
        "water_need": "Medium",
        "description": "Prefers moderate moisture and cooler temperatures."
    },

    {
        "name": "Maize",
        "category": "Cereal",
        "min_moisture": 45,
        "max_moisture": 75,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 18,
        "max_temp": 32,
        "water_need": "Medium",
        "description": "Needs moderate moisture and warm conditions."
    },

    {
        "name": "Millet",
        "category": "Cereal",
        "min_moisture": 20,
        "max_moisture": 50,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 20,
        "max_temp": 35,
        "water_need": "Low",
        "description": "Suitable for relatively dry and warm conditions."
    },

    {
        "name": "Sorghum",
        "category": "Cereal",
        "min_moisture": 25,
        "max_moisture": 55,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 20,
        "max_temp": 35,
        "water_need": "Low",
        "description": "Relatively drought tolerant."
    },

    # =====================================================
    # PULSES
    # =====================================================

    {
        "name": "Chickpea",
        "category": "Pulse",
        "min_moisture": 30,
        "max_moisture": 55,
        "min_ph": 6.0,
        "max_ph": 8.0,
        "min_temp": 15,
        "max_temp": 30,
        "water_need": "Low-Medium",
        "description": "Prefers moderate moisture and well-drained soil."
    },

    {
        "name": "Pigeon Pea",
        "category": "Pulse",
        "min_moisture": 30,
        "max_moisture": 60,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 20,
        "max_temp": 35,
        "water_need": "Medium",
        "description": "Warm-season pulse with moderate water requirement."
    },

    # =====================================================
    # OILSEEDS
    # =====================================================

    {
        "name": "Groundnut",
        "category": "Oilseed",
        "min_moisture": 35,
        "max_moisture": 65,
        "min_ph": 5.5,
        "max_ph": 7.0,
        "min_temp": 22,
        "max_temp": 32,
        "water_need": "Medium",
        "description": "Needs moderate moisture and good drainage."
    },

    {
        "name": "Sunflower",
        "category": "Oilseed",
        "min_moisture": 30,
        "max_moisture": 60,
        "min_ph": 6.0,
        "max_ph": 7.5,
        "min_temp": 18,
        "max_temp": 30,
        "water_need": "Low-Medium",
        "description": "Performs well in moderately moist soil."
    },

    # =====================================================
    # VEGETABLES
    # =====================================================

    {
        "name": "Tomato",
        "category": "Vegetable",
        "min_moisture": 50,
        "max_moisture": 75,
        "min_ph": 5.5,
        "max_ph": 7.0,
        "min_temp": 18,
        "max_temp": 32,
        "water_need": "Medium",
        "description": "Needs consistent moisture and warm conditions."
    },

    {
        "name": "Chilli",
        "category": "Vegetable",
        "min_moisture": 45,
        "max_moisture": 70,
        "min_ph": 5.5,
        "max_ph": 7.0,
        "min_temp": 18,
        "max_temp": 32,
        "water_need": "Medium",
        "description": "Prefers warm weather and moderate moisture."
    },

    {
        "name": "Potato",
        "category": "Vegetable",
        "min_moisture": 45,
        "max_moisture": 70,
        "min_ph": 5.0,
        "max_ph": 6.5,
        "min_temp": 12,
        "max_temp": 25,
        "water_need": "Medium",
        "description": "Prefers cooler temperatures and slightly acidic soil."
    },

    {
        "name": "Onion",
        "category": "Vegetable",
        "min_moisture": 35,
        "max_moisture": 65,
        "min_ph": 6.0,
        "max_ph": 7.5,
        "min_temp": 13,
        "max_temp": 28,
        "water_need": "Medium",
        "description": "Needs controlled moisture and mild temperature."
    },

    {
        "name": "Okra",
        "category": "Vegetable",
        "min_moisture": 45,
        "max_moisture": 70,
        "min_ph": 6.0,
        "max_ph": 7.5,
        "min_temp": 22,
        "max_temp": 35,
        "water_need": "Medium",
        "description": "Warm-season vegetable needing moderate moisture."
    },

    {
        "name": "Cucumber",
        "category": "Vegetable",
        "min_moisture": 55,
        "max_moisture": 80,
        "min_ph": 5.5,
        "max_ph": 7.0,
        "min_temp": 18,
        "max_temp": 32,
        "water_need": "High",
        "description": "Needs regular moisture."
    },

    # =====================================================
    # FRUITS
    # =====================================================

    {
        "name": "Watermelon",
        "category": "Fruit",
        "min_moisture": 40,
        "max_moisture": 65,
        "min_ph": 5.5,
        "max_ph": 7.0,
        "min_temp": 22,
        "max_temp": 35,
        "water_need": "Medium",
        "description": "Warm-season fruit crop."
    },

    {
        "name": "Papaya",
        "category": "Fruit",
        "min_moisture": 45,
        "max_moisture": 70,
        "min_ph": 5.5,
        "max_ph": 7.0,
        "min_temp": 22,
        "max_temp": 35,
        "water_need": "Medium",
        "description": "Prefers warm temperatures and moderate moisture."
    },

    {
        "name": "Banana",
        "category": "Fruit",
        "min_moisture": 60,
        "max_moisture": 85,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 20,
        "max_temp": 35,
        "water_need": "High",
        "description": "Needs warm conditions and good water availability."
    },

    {
        "name": "Mango",
        "category": "Fruit",
        "min_moisture": 30,
        "max_moisture": 65,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 20,
        "max_temp": 35,
        "water_need": "Medium",
        "description": "Warm-climate fruit crop."
    },

    {
        "name": "Grapes",
        "category": "Fruit",
        "min_moisture": 30,
        "max_moisture": 60,
        "min_ph": 5.5,
        "max_ph": 7.5,
        "min_temp": 18,
        "max_temp": 32,
        "water_need": "Medium",
        "description": "Needs moderate moisture and good drainage."
    },

    # =====================================================
    # OTHER PLANTS
    # =====================================================

    {
        "name": "Spinach",
        "category": "Leafy Plant",
        "min_moisture": 50,
        "max_moisture": 75,
        "min_ph": 6.0,
        "max_ph": 7.5,
        "min_temp": 10,
        "max_temp": 24,
        "water_need": "Medium",
        "description": "Prefers moist soil and cooler conditions."
    },

    {
        "name": "Carrot",
        "category": "Vegetable",
        "min_moisture": 45,
        "max_moisture": 70,
        "min_ph": 6.0,
        "max_ph": 7.0,
        "min_temp": 15,
        "max_temp": 25,
        "water_need": "Medium",
        "description": "Needs moderate moisture and loose soil."
    },

    {
        "name": "Peas",
        "category": "Pulse/Vegetable",
        "min_moisture": 45,
        "max_moisture": 70,
        "min_ph": 6.0,
        "max_ph": 7.5,
        "min_temp": 10,
        "max_temp": 25,
        "water_need": "Medium",
        "description": "Prefers cool temperatures and moderate moisture."
    }
]