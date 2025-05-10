import { DataConnect } from 'firebase/data-connect';
export { DataConnect };
export declare const DATA_CONNECT_PROVIDER_NAME = "data-connect";
export interface DataConnectInstances extends Array<DataConnect> {
}
export declare class DataConnectInstances {
    constructor();
}
export declare const dataConnectInstance$: import("rxjs").Observable<DataConnect>;
