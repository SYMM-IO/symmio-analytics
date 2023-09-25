export interface EnvironmentInterface {
	assetsFolder: string;
	aggregate?: boolean;
	environments?: SubEnvironmentInterface[];
}

export interface SubEnvironmentInterface {
	name?: string;
	subgraphUrl?: string;
	collateralDecimal?: number;
	mainColor?: string;
	accountSource?: string;
	fromTimestamp: string | null;
}