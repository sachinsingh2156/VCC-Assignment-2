# **Google Cloud Platform (GCP) Virtual Machine Setup with Auto-Scaling and Security**

## **1. Introduction**
Google Cloud Platform (GCP) provides a robust suite of cloud services that allow businesses to deploy, manage, and scale applications efficiently. One of these services, **Compute Engine**, enables users to provision and manage Virtual Machines (VMs) dynamically. **Auto-scaling** ensures resources adjust based on workload demand, maximizing performance while minimizing costs. Additionally, **Identity and Access Management (IAM)** and **firewall rules** are implemented to secure cloud resources against unauthorized access. This guide details the deployment of a VM instance, the configuration of auto-scaling policies, and essential security settings for scalability and protection.

## **2. Objectives**
This project aims to:
- Deploy a **Virtual Machine (VM) instance** in GCP.
- Configure **Auto-Scaling Policies** to optimize resources dynamically.
- Implement **Security Measures** such as IAM roles and firewall rules.
- Provide a **clear architectural design** representing system interactions.
- Include **source code repositories** for deployment automation.

## **3. Step-by-Step Implementation**

### **3.1 Creating a VM Instance in GCP**
#### **Step 1: Log in to GCP Console**
1. Open a web browser and navigate to **Google Cloud Console**.
2. Sign in with your Google account.

#### **Step 2: Navigate to Compute Engine**
1. Go to **Compute Engine > VM Instances**.
2. Click **Create Instance**.

#### **Step 3: Configure the VM Instance**
1. **Enter Instance Name**: `my-instance`
2. **Select a Region & Zone**: Choose the nearest location.
3. **Choose a Machine Type**: `e2-medium` (2 vCPUs, 4 GB RAM) or adjust as needed.
4. **Boot Disk**: Select **Ubuntu 20.04 LTS**.
5. **Enable Firewall**: Check **Allow HTTP and HTTPS traffic**.
6. Click **Create**.

### **3.2 Configuring Auto-Scaling Policies**
#### **Step 1: Create a Managed Instance Group**
1. Navigate to **Compute Engine > Instance Groups**.
2. Click **Create Instance Group**.

#### **Step 2: Configure the Instance Group**
1. Select **Managed Instance Group**.
2. Choose an **Instance Template**.
3. Enable **Auto-Scaling**.

#### **Step 3: Define Auto-Scaling Policies**
1. **Metric**: CPU utilization.
2. **Target CPU Utilization**: 60%.
3. **Minimum Instances**: 1.
4. **Maximum Instances**: 5.
5. Click **Create**.

### **3.3 Implementing Security Measures**
#### **3.3.1 Setting Up IAM Roles**
1. Go to **IAM & Admin > IAM**.
2. Click **+ Add**.
3. **Enter Member Email** and assign roles:
   - **Compute Viewer**: Read-only access.
   - **Compute Admin**: Full control over Compute Engine resources.
4. Click **Save**.

#### **3.3.2 Configuring Firewall Rules**
1. Navigate to **VPC Network > Firewall**.
2. Click **Create Firewall Rule**.
3. **Enter Rule Name**: `allow-http-ssh`
4. **Target**: Apply to all instances.
5. **Source IPv4 Range**: `0.0.0.0/0` (or restrict as needed).
6. **Allowed Protocols & Ports**:
   - **TCP**: `22, 80, 443`
7. Click **Create**.

## **4. Architecture Design**
![Architecture-diagram](https://github.com/user-attachments/assets/f3ab6997-d669-43fe-a4cc-c77f797a1999)

## **5. Running a Python Program on the VM**
### **Purpose of Implementing a Python Program**
After setting up the VM, it is crucial to verify its functionality. Running a Python program tests the VM’s internet connectivity, installed dependencies, and execution capabilities. The script used is a **web scraper** that fetches website titles, confirming that network requests are processed correctly.

### **Implementation Steps**
#### **Step 1: Clone the Repository**
```sh
git clone https://github.com/sachinsingh2156/VCC-Assignment-2.git
cd VCC-Assignment-2
```

#### **Step 2: Install Dependencies**
```sh
sudo apt update
sudo apt install python3-pip -y
pip3 install requests beautifulsoup4
```

#### **Step 3: Run the Python Web Scraper**
```sh
python3 web_scraper.py
```

#### **Expected Output**
```sh
https://www.python.org --> Welcome to Python.org
https://www.wikipedia.org --> Wikipedia
https://www.github.com --> GitHub: Where the world builds software
```
This output confirms the VM is correctly configured and functional.

## **6. Source Code Repository**
All deployment scripts and configurations are stored in the following repository:
[GitHub Repository](https://github.com/sachinsingh2156/VCC-Assignment-2.git)

