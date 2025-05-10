import { SchedulerAction, SchedulerLike, Subscription } from 'rxjs';
import * as i0 from "@angular/core";
export declare enum LogLevel {
    "SILENT" = 0,
    "WARN" = 1,
    "VERBOSE" = 2
}
export declare const setLogLevel: (logLevel: LogLevel) => LogLevel;
/**
 * Schedules tasks so that they are invoked inside the Zone that is passed in the constructor.
 */
export declare class ɵZoneScheduler implements SchedulerLike {
    private zone;
    private delegate;
    constructor(zone: any, delegate?: any);
    now(): any;
    schedule(work: (this: SchedulerAction<any>, state?: any) => void, delay?: number, state?: any): Subscription;
}
export declare class ɵAngularFireSchedulers {
    readonly outsideAngular: ɵZoneScheduler;
    readonly insideAngular: ɵZoneScheduler;
    constructor();
    static ɵfac: i0.ɵɵFactoryDeclaration<ɵAngularFireSchedulers, never>;
    static ɵprov: i0.ɵɵInjectableDeclaration<ɵAngularFireSchedulers>;
}
export declare const ɵzoneWrap: <T = unknown>(it: T, blockUntilFirst: boolean, logLevel?: LogLevel) => T;
