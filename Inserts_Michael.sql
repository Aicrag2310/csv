--Dat Thanh
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4111,16, 'BLUE SPA LINER', '1006', 12.65, 1, 1, 0);
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4112,16, 'HDPE HEADER BAG', '1007', 11.80, 1, 1, 0);
--Bee Liner
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4113,17, 'Unnotched slipper No Embossed', '1008', 17.30, 1, 1, 0);
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4114,17, 'Toe Separator Eva', '1009', 20.30, 1, 1, 0);
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4115,17, 'Toe Separator Pe', '1010', 11.60, 1, 1, 0);
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4116,17, 'Waxing Roll', '1011', 83.70, 1, 1, 0);
INSERT INTO Product (`id`,`brandId`,`name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES (4117,17, 'Paraffin Bag Roll', '1012', 12.30, 1, 1, 0);

--Dat Thanh
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4111,12.65,16);
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4112,11.8,16);
--Bee Liner
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4113,17.3,17);
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4114,20.3,17);
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4115,11.6,17);
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4116,83.7,17);
INSERT INTO ProductSupplier (`productId`, `priceCost`, `supplierId`) VALUES (4117,12.3,17);

--Dat Thanh
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4111,16);
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4112,2);
--Bee Liner
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4113,16);
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4114,16);
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4115,16);
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4116,2);
INSERT INTO ProductTag (`productId`, `tagId`) VALUES (4117,2);

--Dat Thanh
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4111,0,0, 3500,1);
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4112,0,0, 500,1);
--Bee Liner
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4113,0,0, 650,1);
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4114,0,0, 300,1);
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4115,0,0, 300,1);
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4116,0,0, 50,1);
INSERT INTO `Inventory` (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES (4117,0,0, 200,1);

