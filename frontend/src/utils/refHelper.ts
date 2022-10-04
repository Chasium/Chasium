import type {
    ComponentOptionsBase,
    ComponentPublicInstance,
    ComputedOptions,
    MethodOptions,
} from 'vue';

export function refHelper<
    D,
    C extends ComputedOptions,
    M extends MethodOptions
>(
    parent: ComponentPublicInstance,
    refName: string,
    _refClass: ComponentOptionsBase<any, any, D, C, M, any, any, any, any, any>
) {
    return parent.$refs[refName] as ComponentPublicInstance<
        unknown,
        unknown,
        D,
        C,
        M
    >;
}
