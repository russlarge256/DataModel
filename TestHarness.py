# Desc: Python 210 Final DataModel
# ChangeLog: (When,Who,What)
# 3/17/2019, RLarge, Created & Modified Script



# Processor Modules
from DataProcessor import InventoryProcessor as IP
from DataProcessor import DBProcessor as dp
from DataProcessor import ProductsProcessor as PP
from DataProcessor import InventoryCountProcessor as ICP

# DataModel Modules
from DataModel import Product as Prod
from DataModel import InventoryCount as IC
from DataModel import Inventory as Inv


# from DBProcessor import Product as Prod
debugDP = False
debugIP = False
debugPP = False
debugICP = False
debugProd = False
debugIC = False

if __name__ == '__main__':

    if debugDP == True:
        try:
            dp.check_for_or("SELECT * FROM T1 WHERE ID = 1 or 1 = 1")
        except Exception as e: print(e)
        try:
            dp.check_for_extra_semicolon("SELECT * ;Delete From T1; FROM T1;")
        except Exception as e: print(e)
        try:
            dp.check_for_date('01/01/2000')
        except Exception as e: print(e)

        dbp = dp(':memory:')
        print(dbp.build_ins_code())
        print(dbp.build_upd_code())
        print(dbp.build_del_code())
        print(dbp.build_sel_code())
        print(dbp.build_sel_code())
        dbp.db_con.close()


    if debugIP == True:
        ip = IP(':memory:')
        print(ip.build_ins_code(inventory_id=1, inventory_date='2000-01-01'))
        print(ip.build_upd_code(inventory_id=1, inventory_date='2000-02-02'))
        print(ip.build_del_code(inventory_id=1))
        print(ip.build_sel_code())

        # Create a table for testing
        crs = ip.db_con.cursor()
        crs.execute("CREATE TABLE Inventories (InventoryID int, InventoryDate date);")
        ip.db_con.commit()
        for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
            print(row)
        ip.db_con.commit()

        # Test SQL Transactions
        ip.execute_sql_code(ip.build_ins_code(inventory_id=1, inventory_date='2000-01-01')).close()
        for row in ip.execute_sql_code(ip.build_sel_code()):
            print(row)

        ip.execute_sql_code(ip.build_upd_code(inventory_id=1, inventory_date='2000-02-02')).close()
        for row in ip.execute_sql_code(ip.build_sel_code(inventory_id=1)):
            print(row)

        ip.execute_sql_code(ip.build_del_code(inventory_id=1)).close()
        for row in ip.execute_sql_code(ip.build_sel_code()):
            print(row)

    if debugICP == True:

        # from DBProcessor import InventoryCountProcessor as ICP
        icp = ICP(':memory:')
        print(icp.build_ins_code(inventory_count=25, product_name='chair'))
        print(icp.build_upd_prod_code(inventory_count=30, product_name='desk'))
        print(icp.build_upd_inv_code(inventory_count=35, product_name='hanger'))
        print(icp.build_sel_prod_code(product_name='hanger'))
        print(icp.build_sel_inv_count_code(inventory_count=30))
        print(icp.build_del_code(product_name='hanger'))

        # Create a table for testing
        crs = icp.db_con.cursor()
        crs.execute("CREATE TABLE InventoryCount (Count INTEGER, ProductName TEXT);")
        icp.db_con.commit()
        for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
            print(row)
        icp.db_con.commit()


        # # Test SQL Transactions
        icp.execute_sql_code(icp.build_ins_code(inventory_count=25, product_name='hanger')).close()
        for row in icp.execute_sql_code(icp.build_sel_prod_code(product_name='hanger')):
            print(row)

        icp.execute_sql_code(icp.build_upd_prod_code(inventory_count=25, product_name='newhanger')).close()
        for row in icp.execute_sql_code(icp.build_sel_inv_count_code(inventory_count=25)):
            print(row)

        icp.execute_sql_code(icp.build_upd_inv_code(inventory_count=30, product_name='newhanger')).close()
        for row in icp.execute_sql_code(icp.build_sel_inv_count_code(inventory_count=30)):
            print(row)


    if debugPP == True:

        pp = PP(':memory:')
        print(pp.build_ins_code(product_id=132, product_name='hanger'))
        print(pp.build_upd_code(product_id=132, product_name='desk'))
        print(pp.build_sel_code(product_id=132))
        print(pp.build_del_code(product_id=132))

        # Create a table for testing
        crs = pp.db_con.cursor()
        crs.execute("CREATE TABLE Products (ProductID INTEGER, ProductName TEXT);")
        pp.db_con.commit()
        for row in crs.execute("Select name, sql From sqlite_master Where type='table;'"):
            print(row)
        pp.db_con.commit()

        # # Test SQL Transactions
        pp.execute_sql_code(pp.build_ins_code(product_id=25, product_name='hanger')).close()
        for row in pp.execute_sql_code(pp.build_sel_code(product_id=25)):
            print(row)

        pp.execute_sql_code(pp.build_upd_code(product_id=25, product_name='table')).close()
        for row in pp.execute_sql_code(pp.build_sel_code(product_id=25)):
            print(row)

        pp.execute_sql_code(pp.build_del_code(product_id=25)).close()
        for row in pp.execute_sql_code(pp.build_sel_code()):
            print(row)

    if debugProd == True:

        p1 = Prod(100, "Mouse")
        p2 = Prod(200, "Keyboard")

        print(p1)

        try:
            Prod('A', "Alpha")
        except Exception as e:
            print(e)
        try:
            Prod(1.2, "Float")
        except Exception as e:
            print(e)
        try:
            Prod(0, "Zero")
        except Exception as e:
            print(e)
        try:
            Prod(-1, "LT Zero")
        except Exception as e:
            print(e)

    if debugIC == True:

        try:
            p1 = Prod(100, "ProdA")
            p2 = Prod(200, "ProdB")
            ic1 = IC(p1, 15)
            ic2 = IC(p2, 45)
            invJan0119 = Inv(1, '2020-01-01', [ic1, ic2])
            count = 1
            for ic in invJan0119.inventory_counts:
                print("Dataset {}:'\n'"
                      "InventoryDate: {}'\n'"
                      "InventoryID: {}'\n'"
                      "Product Name: {}'\n'"
                      "Product Inv Count {}'\n'"
                      "".format(count, invJan0119.inventory_date, invJan0119.inventory_id, ic.product.product_name,
                                ic.product_inventory_count))
                count += 1

        except TypeError:
            print("Type error")
        except Exception as e:
            print(e)

