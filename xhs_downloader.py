from asyncio import run

from rich import print

from source import XHS


async def download_xhs(
        url: str,
        download: bool = True,
        index: list = None,
        work_path: str = "./",
        folder_name: str = "Download",
        name_format: str = "作品标题 作品描述",
        user_agent: str = "",
        cookie: str = "",
        proxy: str = None,
        timeout: int = 10,
        chunk: int = 1024 * 1024 * 10,
        max_retry: int = 5,
        record_data: bool = False,
        image_format: str = "PNG",
        folder_mode: bool = False,
        image_download: bool = True,
        video_download: bool = True,
        live_download: bool = False,
        download_record: bool = False,
        language: str = "zh_CN",
        author_archive: bool = True,
        read_cookie: str = None,
):
    """
    小红书内容下载器，支持图文/视频/动图下载
    
    参数:
        url: str - 小红书作品链接
        download: bool - 是否下载作品文件，默认为True
        index: list - 可选，指定下载特定索引的内容，如[1,2,3]
        work_path: str - 作品数据/文件保存根路径，默认为当前目录
        folder_name: str - 作品文件储存文件夹名称，默认为Download
        name_format: str - 文件命名格式
        user_agent: str - 自定义User-Agent
        cookie: str - 小红书网页版Cookie，无需登录，可选参数
        proxy: str - 网络代理，如"http://127.0.0.1:7890"
        timeout: int - 请求数据超时限制(秒)
        chunk: int - 下载文件时每次获取的数据块大小(字节)
        max_retry: int - 请求数据失败时重试的最大次数
        record_data: bool - 是否保存作品数据至文件
        image_format: str - 图文作品文件下载格式，支持AUTO、PNG、WEBP、JPEG、HEIC
        folder_mode: bool - 是否将每个作品的文件储存至单独的文件夹
        image_download: bool - 图文作品文件下载开关
        video_download: bool - 视频作品文件下载开关
        live_download: bool - 图文动图文件下载开关
        download_record: bool - 是否记录下载成功的作品ID
        language: str - 设置程序提示语言
        author_archive: bool - 是否将每个作者的作品存至单独的文件夹
        read_cookie: str - 读取浏览器Cookie，支持设置浏览器名称(字符串)或浏览器序号(整数)
    
    返回:
        dict: 作品详细信息，包括下载地址
    """
    async with XHS(
            work_path=work_path,
            folder_name=folder_name,
            name_format=name_format,
            user_agent=user_agent,
            cookie=cookie,
            proxy=proxy,
            timeout=timeout,
            chunk=chunk,
            max_retry=max_retry,
            record_data=record_data,
            image_format=image_format,
            folder_mode=folder_mode,
            image_download=image_download,
            video_download=video_download,
            live_download=live_download,
            download_record=download_record,
            language=language,
            read_cookie=read_cookie,
            author_archive=author_archive,
    ) as xhs:
        result = await xhs.extract(url, download, index=index)
        return result


async def main():
    """测试下载器功能"""
    url = "https://www.xiaohongshu.com/explore/67fc8571000000000b02ed97?xsec_token=ABhAGGFUI7PnadcWR3_mFR3uI-4lXwWqXDorNVB5RyaYo=&xsec_source=pc_search&m_source=itab&source=web_explore_feed"
    read_cookie = "chrome"
    # 测试默认配置下载
    result = await download_xhs(url=url, read_cookie=read_cookie)
    print("下载结果:", result)

    # 可选：测试特定配置
    # result = await download_xhs(
    #     url,
    #     download=True,
    #     index=[1, 2],  # 只下载第1和第2个文件
    #     folder_name="XHS_Download",
    #     download_record=False,
    # )
    # print("特定配置下载结果:", result)


if __name__ == "__main__":
    run(main())
