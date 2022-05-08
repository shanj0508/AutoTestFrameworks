import pytest

def run():
    pytest.main(['-s', '-v', './test_cases/test_shop_pom_V2.py',
                 "--maxfail", "5",
                 "-m","slow"
                 ])

if __name__ == '__main__':
    run()