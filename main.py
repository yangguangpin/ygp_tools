import webview
import os
import sys
import base64


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
            result = self.window.create_file_dialog(
                webview.SAVE_DIALOG,
                directory=os.path.expanduser('~'),
                save_filename=filename
            )
            if result:
                if isinstance(result, tuple):
                    result = result[0]
                content = base64.b64decode(content_base64)
                with open(result, 'wb') as f:
                    f.write(content)
                return {'success': True, 'path': result}
            return {'success': False, 'message': '用户取消保存'}
        except Exception as e:
            return {'success': False, 'message': str(e)}


def main():
    # 读入 HTML 内容，通过 html 参数直接传入，避免文件 I/O 造成的启动白屏
    html_path = get_resource_path('index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    api = Api()
    window = webview.create_window(
        'YGP工具箱',
        html=html_content,
        width=1100,
        height=700,
        min_size=(900, 600),
        resizable=True,
        js_api=api,
        background_color='#6e64c6'  # splash渐变(667eea→764ba2)的中间色, 过渡更平滑
    )
    api.window = window
    webview.start()


if __name__ == '__main__':
    main()
