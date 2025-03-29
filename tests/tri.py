# New pyo library use "TriangleTable" instead of "TriTable" to 
# generate Triangle waves

# --- See which one does your pyo version supports ---

import pyo
print("TriangleTable in pyo?", hasattr(pyo, 'TriangleTable'))  # Should return True
print("TriTable in pyo?", hasattr(pyo, 'TriTable'))  # Likely False