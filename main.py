from utils.config import settings
from tools.linker import link_merchant_identification
import time

def main():
    start = time.perf_counter()
    wid = settings.warehouse_id
    
    link_merchant_identification(
        settings.w, 
        wid, 
        "Test_Cafe", 
        "acct_123", 
        "ic_456"
    )
    
    end = time.perf_counter()
    elapsed_time = end - start
    print(f'runtime: {elapsed_time}')
    
if __name__ == "__main__":
    main()
