declare module '@uwdata/vgplot' {
    export function wasmConnector(): any;
    export function socketConnector(uri: string): any;
    export function restConnector(uri: string): any;
    export function coordinator(): {
        databaseConnector(connector: any): Promise<void>;
        exec(query: any): Promise<void>;
    };
    export function loadCSV(tableName: string, fileName: string): any;
    export function loadParquet(tableName: string, fileName: string): any;
    export function plot(...args: any[]): any;
    export function areaY(data: any, options: { x: string; y: string }): any;
    export function from(tableName: string): any;
    // Add other functions or types you use from this module
}