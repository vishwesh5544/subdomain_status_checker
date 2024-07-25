from subdomain_checker import SubdomainChecker

if __name__ == "__main__":

    try: 
        checker = SubdomainChecker("subdomains.json")
        checker.run()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
