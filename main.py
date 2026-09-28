from cli import AppContext, MenuRouter

def main():
    context = AppContext()
    router = MenuRouter(context)
    router.run()

if __name__ == "__main__":
    main()