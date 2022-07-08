from ds4.sharepoint.context import get_context


def create_folders(names):
    data = {}
    ctx = get_context()
    for name in names:
        result = ctx.web.folders.add(f"Freigegebene Dokumente/{name}").execute_query()
        print("result: ", result)
        data[name] = result
    return data
