import webview
import os
import sys
import base64
from webview.window import Window


def get_resource_path(relative_path):
    """获取资源文件路径，兼容开发环境和PyInstaller打包后环境"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)


class Api:
    """暴露给JavaScript的API"""

    def save_xlsx_file(self, params):
        """保存XLSX文件"""
        filename = params.get('filename', 'output.xlsx')
        content_base64 = params.get('content', '')

        try:
            # 打开文件保存对话框
            result = self.window.create_file_dialog(
                webview.SAVE_DIALOG,
                directory=os.path.expanduser('~'),
                save_filename=filename
            )
            if result:
                # 如果返回的是tuple，取第一个元素
                if isinstance(result, tuple):
                    result = result[0]
                # 解码base64内容并写入文件
                content = base64.b64decode(content_base64)
                with open(result, 'wb') as f:
                    f.write(content)
                return {'success': True, 'path': result}
            return {'success': False, 'message': '用户取消保存'}
        except Exception as e:
            return {'success': False, 'message': str(e)}


def main():
    html_path = get_resource_path('index.html')
    api = Api()
    window = webview.create_window(
        'YGP工具箱',
        html_path,
        width=1100,
        height=700,
        min_size=(900, 600),
        resizable=True,
        js_api=api
    )
    api.window = window
    webview.start()


if __name__ == '__main__':
    main()
