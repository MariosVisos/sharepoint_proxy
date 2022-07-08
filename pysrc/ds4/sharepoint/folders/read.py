from pprint import pprint

from ds4.sharepoint.context import get_context


def enum_folder(parent_folder, action):
    """
    :type parent_folder: Folder
    :type action: (Folder)-> None
    """
    parent_folder.expand(["Folders"]).get().execute_query()
    action(parent_folder)
    for folder in parent_folder.folders:
        enum_folder(folder, action)


def print_folder_stat(folder):
    """
    :type folder: Folder
    """
    # print("content_type_order:", folder.content_type_order)
    # print("unique_content_type_order:", folder.unique_content_type_order)
    print("parent_folder:", folder.parent_folder)
    print("exists:", folder.exists)
    print("name:", folder.name)
    print("resource_path:", folder.resource_path)
    print("server_relative_path:", folder.server_relative_path)
    print("serverRelativeUrl:", folder.serverRelativeUrl)
    print("time_created:", folder.time_created)
    print("time_last_modified:", folder.time_last_modified)
    print("unique_id:", folder.unique_id)
    print("storage_metrics:", folder.storage_metrics)
    # pprint(dir(folder.s
    # torage_metrics))
    # pprint(folder.storage_metrics.tojson)
    # print("storage_metrics.last_modified:", folder.storage_metrics.last_modified)
    # print("storage_metrics.total_file_count:", folder.storage_metrics.total_file_count)
    # print(
    #     "storage_metrics.total_file_stream_size:",
    #     folder.storage_metrics.total_file_stream_size,
    # )
    # print("storage_metrics.total_size:", folder.storage_metrics.total_size)
    print("\n")


def get_folders():
    ctx = get_context()
    root_folder = ctx.web.default_document_library().root_folder

    # site = ctx.site.get().execute_query()
    # print("Site url: {}".format(site.url))
    # print("server_relative_url", site.server_relative_url)
    # print("server_relative_path", site.server_relative_path)
    # print("usage_info", site.usage_info)
    # print("features", site.features)
    # print("classification", site.classification)
    # print("root_web", site.root_web.web_infos)
    # print("root_web.webs", site.root_web.webs)
    # print("root_web.site_user_info_list", site.root_web.site_user_info_list)
    # print(
    #     "root_web.site_collection_app_catalog",
    #     site.root_web.site_collection_app_catalog,
    # )
    # pprint(dir(site))
    # pprint(dir(site.root_web))
    enum_folder(root_folder, print_folder_stat)
