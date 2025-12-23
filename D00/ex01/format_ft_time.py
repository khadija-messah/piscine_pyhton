import time
from datetime import datetime

curence = time.time()
print(f"Seconds since January 1, 1970: {curence:,.4f} or {curence:.2e} in scientific notation")

now = datetime.now()
print(now.strftime("%b %d %Y"))
