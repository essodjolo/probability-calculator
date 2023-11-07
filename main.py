import test_module

if __name__ == '__main__':
    print("Running unit tests...")

    exec("test_module")

    testing = test_module.MyTestCase()

    testing.test_draw()
    testing.test_experiment()

    print("Done.")
