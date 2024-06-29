#
# spec file for package obs-service-cpanspec
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           obs-service-cpanspec
Summary:        An OBS source service: Create spec files for cpan sources
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        0.3
Release:        0
Source0:        cpanspec
Source1:        cpanspec.service
Source2:        LICENSE
Requires:       bzip2
Requires:       cpanspec
BuildArch:      noarch
BuildRequires:  (perl-generators or rpm-build-perl)
BuildRequires:  rpm_macro(_obs_service_dir)
Requires:       perl(Module::Build)
%{!?__perl_requires:%define __perl_requires %{_rpmconfigdir}/perl.req}

%description
This is a source service for openSUSE Build Service.

It's a wrapper around cpanspec script

%prep
%setup -q -D -T 0 -c
sed -i 's~/usr/bin~%{_bindir}~' %{SOURCE0}

%build

%install
install -Dm 0755 %{SOURCE0} %{buildroot}%{_obs_service_dir}/cpanspec
install -Dm 0644 %{SOURCE1} %{buildroot}%{_obs_service_dir}/cpanspec.service
install -Dm 0644 %{SOURCE2} %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE

%files
%attr(755, root, root) %{_obs_service_dir}/cpanspec
%attr(644, root, root) %{_obs_service_dir}/cpanspec.service
%license LICENSE
%changelog
