import { EnvironmentProviders, Injector, NgZone } from '@angular/core';
import { FirebaseApp } from '@angular/fire/app';
import { DataConnect } from './data-connect';
import * as i0 from "@angular/core";
export declare function defaultDataConnectInstanceFactory(provided: DataConnect[] | undefined, defaultApp: FirebaseApp): DataConnect;
export declare function dataConnectInstanceFactory(fn: (injector: Injector) => DataConnect): (zone: NgZone, injector: Injector) => DataConnect;
export declare class DataConnectModule {
    constructor();
    static ɵfac: i0.ɵɵFactoryDeclaration<DataConnectModule, never>;
    static ɵmod: i0.ɵɵNgModuleDeclaration<DataConnectModule, never, never, never>;
    static ɵinj: i0.ɵɵInjectorDeclaration<DataConnectModule>;
}
export declare function provideDataConnect(fn: (injector: Injector) => DataConnect, ...deps: any[]): EnvironmentProviders;
