#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-digest
Version  : 1.0
Release  : 2
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-digest-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-digest package.
Group: Data

%description data
data components for the mvn-plexus-digest package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-digest/1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-digest/1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-digest/1.0/plexus-digest-1.0.pom
