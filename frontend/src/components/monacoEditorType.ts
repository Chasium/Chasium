//import { PropType } from 'vue';

export type Theme = 'vs' | 'hc-black' | 'vs-dark';
export type FoldingStrategy = 'auto' | 'indentation';
export type RenderLineHighlight = 'all' | 'line' | 'none' | 'gutter';
export interface Options {
    automaticLayout: boolean; // 自适应布局
    foldingStrategy: FoldingStrategy; // 折叠方式  auto | indentation
    renderLineHighlight: RenderLineHighlight; // 行亮
    selectOnLineNumbers: boolean; // 显示行号
    minimap: {
        // 关闭小地图
        enabled: boolean;
    };
    readOnly: boolean; // 只读
    fontSize: number; // 字体大小
    scrollBeyondLastLine: boolean; // 取消代码后面一大段空白
    overviewRulerBorder: boolean; // 不要滚动条的边框
}

export const editorProps = {
    modelValue: {
        type: String,
        default: '/* Please enter your script here :) */',
    },
    width: {
        type: [String, Number],
        default: '100%',
    },
    height: {
        type: [String, Number],
        default: '100%',
    },
    language: {
        type: String,
        default: 'javascript',
    },
    theme: {
        type: String,
        validator(value: string): boolean {
            return ['vs', 'hc-black', 'vs-dark'].includes(value);
        },
        default: 'vs',
    },
    options: {
        type: Object,
        default: function () {
            return {
                automaticLayout: true,
                foldingStrategy: 'indentation',
                renderLineHighlight: 'all',
                selectOnLineNumbers: true,
                minimap: {
                    enabled: true,
                },
                readOnly: false,
                fontSize: 16,
                scrollBeyondLastLine: false,
                overviewRulerBorder: false,
            };
        },
    },
};
