# Desc: Python 210 Final DataModel
# ChangeLog: (When,Who,What)
# 3/17/2019, RLarge, Created & Modified Script

import tkinter as tk
from tkinter import ttk
import DataModel as DM
import DataProcessor as DP


class IOProcessor():


###############################################
#-------PRODUCTS tkinter processing----------#
###############################################

    @staticmethod
    def sel_product(text_widget):
        products = []
        pp = DP.ProductsProcessor('Python210FinalDB.db')
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            products.append(DM.Product(row[0], row[1]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if products is None:
            text_widget.insert("No data available")

        if products is not None:
            text_widget.insert(tk.END, "ProductID | ProductName\n")
            for row in products:
                text_widget.insert(tk.END, str(row) + "\n")
        text_widget['state'] = 'disabled'


    @staticmethod
    def ins_product(product_id, product_name, update_controls=[None]):
        pp = DP.ProductsProcessor('Python210FinalDB.db')
        sql = pp.build_ins_code(product_id=product_id, product_name=product_name)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    @staticmethod
    def upd_product(product_id, product_name, update_controls=[None]):
        pp = DP.ProductsProcessor('Python210FinalDB.db')
        sql = pp.build_upd_code(product_id=product_id, product_name=product_name)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    @staticmethod
    def del_product(product_id, update_controls=[None]):
        pp = DP.ProductsProcessor('Python210FinalDB.db')
        sql = pp.build_del_code(product_id=product_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])
###############################################
#-------INVENTORY tkinter processing----------#
###############################################

    @staticmethod
    def sel_inventory(text_widget):
        inventory = []
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            inventory.append(DM.Inventory(row[0], row[1]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if inventory is None:
            text_widget.insert("No data available")

        if inventory is not None:
            text_widget.insert(tk.END, "InventoryID | InventoryDate\n")
            for row in inventory:
                text_widget.insert(tk.END, str(row) + "\n")
        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_inventory(inventory_id, inventory_date, update_controls=[None]):
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_ins_code(inventory_id=inventory_id, inventory_date=inventory_date)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is None:
            IOProcessor.sel_inventory(update_controls[0])
        if update_controls is not None:
            # Needs work, cannot allow inventory to repopulate new data
            IOProcessor.sel_inventory(update_controls[0])

    @staticmethod
    def upd_inventory(inventory_id, inventory_date, update_controls=[None]):
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_upd_code(inventory_id=inventory_id, inventory_date=inventory_date)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])

    @staticmethod
    def del_inventory(inventory_id, update_controls=[None]):
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_del_code(inventory_id=inventory_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])


######################################################
#-------INVENTORY COUNTS tkinter processing----------#
######################################################

    @staticmethod
    def sel_inventorycounts(text_widget):
        inventorycounts = []
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            inventorycounts.append(DM.InventoryCount(row[0], row[1], row[2]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if inventorycounts is None:
            text_widget.insert("No data available")

        if inventorycounts is not None:
            text_widget.insert(tk.END, "Inventory ID | Product ID | Count\n")
            for row in inventorycounts:
                text_widget.insert(tk.END, str(row) + "\n")
        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_inventory_counts(inventory_id, product_inventory_count, product_id, update_controls=[None]):
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_ins_code(inventory_id=inventory_id, product_inventory_count=product_inventory_count,
                                product_id=product_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventorycounts(update_controls[0])

    @staticmethod
    def upd_inventory_counts(inventory_id, product_inventory_count, product_id, update_controls=[None]):
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_upd_code(inventory_id=inventory_id, product_inventory_count=product_inventory_count,
                                product_id=product_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventorycounts(update_controls[0])


    @staticmethod
    def del_inventory_counts(inventory_id, update_controls=[None]):
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_del_code(inventory_id=inventory_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventorycounts(update_controls[0])



######################################################
#-------          MAIN WINDOW              ----------#
######################################################



class MainWindow():
    """
     -- window_root tk.TK
       -- notebook_frame ttk.Notebook
          -- tab_products tk.Frame
             -- 'Create Header': lbl_product_info ttk.label
             -- 'Create Select Button': btn_sel_product_info ttk.button
             -- 'Create Product ID label/text box': lbl_product_id ttk.label/ttk.entry
             -- 'Create Product Name label/text box': lbl_product_name ttk.label/ttk.entry
             -- 'Create insert button w/ text.get()': ins_prod ttk.button
             -- 'Create update button w/ text.get()': upd_prod ttk.button
             -- 'Create delete button w/ text.get()': del_prod ttk.button
          -- tab_inventories tk.Frame
          -- tab_inventory_counts tk.Frame

    """



    def __init__(self):
        self.window =tk.Tk() # creates root node attribute
        self.window.title("Inventory Manager")
        self.window['padx'] = 20
        self.window['pady'] = 20
        # self.products_widgets()
        self.notebook = ttk.Notebook(self.window)
        self.configure_notebook(self.notebook)


    def configure_notebook(self, notebook_frame):
        notebook_frame.grid(row=1, column=1, sticky=tk.W, padx=20, pady=10)
        self.products_tab(notebook_frame)
        self.inventories_tab(notebook_frame)
        self.inventory_counts_tab(notebook_frame)

        return notebook_frame

    def products_tab(self, notebook_frame):

        # Create Header
        tab_products = tk.Frame(notebook_frame)
        notebook_frame.add(tab_products, text="Products", compound=tk.TOP)

        # Create 'Select' Button
        btn_sel_product_info = ttk.Button(tab_products, text="Select Product Info", width=20)
        btn_sel_product_info.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        btn_sel_product_info["command"] = lambda: IOProcessor.sel_product(mtx_product_info)


        # Create text display
        mtx_product_info = tk.Text(tab_products, width=55, height=10)
        mtx_product_info.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5, columnspan=4)


        # Create Product ID label/text box
        label_product_id = ttk.Label(tab_products, text="Product ID:", width=20)
        label_product_id.grid(row=2, column=0, sticky=tk.W)
        text_product_id = ttk.Entry(tab_products, width=20)
        text_product_id.grid(row=2, column=1)

        # Create Product Name label/text box
        label_product_name = ttk.Label(tab_products, text="Product Name:", width=20)
        label_product_name.grid(row=3, column=0, sticky=tk.W)
        text_product_name = ttk.Entry(tab_products, width=20)
        text_product_name.grid(row=3, column=1)


        # Create Insert button w/ text.get()
        btn_ins_product_info = ttk.Button(tab_products, text="Insert Product Info")
        btn_ins_product_info.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        btn_ins_product_info["command"] = lambda: IOProcessor.ins_product(text_product_id.get(),
                                                                          text_product_name.get(),
                                                                          [mtx_product_info])
        # Create Update button w/ text.get()
        btn_upd_product_info = ttk.Button(tab_products, text="Update Product Info")
        btn_upd_product_info.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        btn_upd_product_info["command"] = lambda: IOProcessor.upd_product(text_product_id.get(),
                                                                          text_product_name.get(),
                                                                          [mtx_product_info])

        # delete button w text entry
        btn_del_product_info = ttk.Button(tab_products, text="Delete Product Info", width=20)
        btn_del_product_info.grid(row=5, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_product_info["command"] = lambda: IOProcessor.del_product(text_product_id.get(),
                                                                          [mtx_product_info])


    def inventories_tab(self, notebook_frame):

        # Create Header
        tabinv = tk.Frame(notebook_frame)
        notebook_frame.add(tabinv, text="Inventory", compound=tk.TOP)

        # Create text display
        mtx_inventory_info = tk.Text(tabinv, width=55, height=10)
        mtx_inventory_info.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5, columnspan=4)

        # Create 'Select' Button
        btn_sel_inv_info = ttk.Button(tabinv, text="Select Inventory Info", width=20)
        btn_sel_inv_info.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        btn_sel_inv_info["command"] = lambda: IOProcessor.sel_inventory(mtx_inventory_info)

        # Create Inventory ID label/text box
        label_inventory_id = ttk.Label(tabinv, text="Inventory ID:", width=20)
        label_inventory_id.grid(row=2, column=0, sticky=tk.W)
        text_inventory_id = ttk.Entry(tabinv, width=20)
        text_inventory_id.grid(row=2, column=1)

        # Create Inventory Date label/text box
        label_inventory_date = tk.Label(tabinv, text="Inventory Date:", width=20)
        label_inventory_date.grid(row=3, column=0, sticky=tk.W)
        text_inventory_date = ttk.Entry(tabinv, width=20)
        text_inventory_date.grid(row=3, column=1)

        # Create Update Button w/ text.get()
        btn_upd_inventory_info = ttk.Button(tabinv, text="Update Inventory Info")
        btn_upd_inventory_info.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        btn_upd_inventory_info["command"] = lambda: IOProcessor.upd_inventory(text_inventory_id.get(),
                                                                              text_inventory_date.get(),
                                                                              [mtx_inventory_info])
        # Create Insert Button w/ text.get()
        btn_ins_inventory_info = ttk.Button(tabinv, text="Insert Inventory Info")
        btn_ins_inventory_info.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        btn_ins_inventory_info["command"] = lambda: IOProcessor.ins_inventory(text_inventory_id.get(),
                                                                              text_inventory_date.get(),
                                                                              [mtx_inventory_info])

        # Create Delete Button w/ text.get()
        btn_del_inventory_info = ttk.Button(tabinv, text="Delete Inventory Info")
        btn_del_inventory_info.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)
        btn_del_inventory_info["command"] = lambda: IOProcessor.del_inventory(text_inventory_id.get(),
                                                                              [mtx_inventory_info])

    def inventory_counts_tab(self, notebook_frame):

        # Create Header
        tabinvcount = tk.Frame(notebook_frame)
        notebook_frame.add(tabinvcount, text="Inventory count", compound=tk.TOP)

        # Create text display
        mtx_inventory_info = tk.Text(tabinvcount, width=55, height=10)
        mtx_inventory_info.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5, columnspan=4)

        # Create 'Select' Button
        btn_sel_inv_count_info = ttk.Button(tabinvcount, text="Select Inventory Info", width=20)
        btn_sel_inv_count_info.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        btn_sel_inv_count_info["command"] = lambda: IOProcessor.sel_inventorycounts(mtx_inventory_info)

        # Create Inventory Count ID label/text box
        label_inventory_id = ttk.Label(tabinvcount, text="Inventory ID:", width=20)
        label_inventory_id.grid(row=2, column=0, sticky=tk.W)
        text_inventory_id = ttk.Entry(tabinvcount, width=20)
        text_inventory_id.grid(row=2, column=1)

        # Create Product ID label/text box
        label_product_id = tk.Label(tabinvcount, text="Product ID:", width=20)
        label_product_id.grid(row=3, column=0, sticky=tk.W)
        text_product_id = ttk.Entry(tabinvcount, width=20)
        text_product_id.grid(row=3, column=1)

        # Create Inventory Count label/text box
        label_inventory_count = tk.Label(tabinvcount, text="Inventory Count:", width=20)
        label_inventory_count.grid(row=4, column=0, sticky=tk.W)
        text_inventory_count = ttk.Entry(tabinvcount, width=20)
        text_inventory_count.grid(row=4, column=1)

        # Create Insert Button w/ text.get()
        btn_ins_inventory_count_info = ttk.Button(tabinvcount, text="Insert Inventory data")
        btn_ins_inventory_count_info.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        btn_ins_inventory_count_info["command"] = lambda: IOProcessor.ins_inventory_counts(text_inventory_id.get(),
                                                                                           text_inventory_count.get(),
                                                                                           text_product_id.get(),
                                                                                           [mtx_inventory_info])

        # Create Update Button w/ text.get()
        btn_upd_inventory_count_info = ttk.Button(tabinvcount, text="Update Inventory Count")
        btn_upd_inventory_count_info.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        btn_ins_inventory_count_info["command"] = lambda: IOProcessor.upd_inventory_counts(text_inventory_id.get(),
                                                                                           text_inventory_count.get(),
                                                                                           text_product_id.get(),
                                                                                           [mtx_inventory_info])

        # Create Delete Button w/ text.get()
        btn_del_inventory_info = ttk.Button(tabinvcount, text="Delete Inventory Count")
        btn_del_inventory_info.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)
        btn_del_inventory_info["command"] = lambda: IOProcessor.del_inventory_counts(text_inventory_id.get(),
                                                                                   [mtx_inventory_info])




if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()


